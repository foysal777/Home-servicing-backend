from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
import jwt
from .serializers import LoginSerializer
from django.conf import settings
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            return Response({"error": "User already exists!"}, status=status.HTTP_400_BAD_REQUEST)

        # Create an inactive user (not saved in admin yet)
        user = User.objects.create_user(email=email, username=username, password=password)
        user.is_active = False
        user.is_verified = False  # Ensure this field exists in the model!
        user.save()

        # Generate JWT token for email verification
        token = jwt.encode({"email": user.email}, settings.SECRET_KEY, algorithm="HS256")

        # Send verification email
        verification_link = f"http://127.0.0.1:8000/authentications/verify-email/{token}/"
        send_mail(
            "Verify Your Email",
            f"Click the link to verify your email: {verification_link}",
            "your-email@gmail.com",  # Make sure this email is valid
            [email],
            fail_silently=False,
        )

        return Response({"message": "Verification email sent!"}, status=status.HTTP_201_CREATED)


class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            # Decode the token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            email = payload["email"]

            # Get user by email
            user = get_object_or_404(User, email=email)

            if user.is_verified:
                return Response({"message": "User already verified."}, status=status.HTTP_400_BAD_REQUEST)

            # Mark the user as verified
            user.is_verified = True
            user.is_active = True  # Now activate user
            user.save()

            return redirect("http://localhost:5173/login")  #login page redirect hobe

        except jwt.ExpiredSignatureError:
            return Response({"error": "Activation link expired!"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({"error": "Invalid token!"}, status=status.HTTP_400_BAD_REQUEST)




class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "access": access_token,
                "refresh": str(refresh),
                "is_superuser": user.is_superuser,
                "is_staff": user.is_staff,
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
