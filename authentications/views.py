# views.py
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer
import jwt
from django.conf import settings

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token = jwt.encode({'email': user.email}, settings.SECRET_KEY, algorithm='HS256')
        verification_url = f"http://localhost:3000/verify-email/{token}/"
        send_mail(
            "Verify Your Email",
            f"Click the link to verify your email: {verification_url}",
            "your_email@gmail.com",
            [user.email],
            fail_silently=False,
        )

class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            email = decoded_data.get("email")
            user = get_object_or_404(User, email=email)
            user.is_active = True
            user.save()
            return Response({"message": "Email verified successfully"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({"error": "Activation link expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
