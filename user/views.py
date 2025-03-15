from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from authentications.models import CustomUser  # Ensure CustomUser is imported

class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]  # Ensure authentication is required

    def get(self, request):
        user = request.user  # JWT token থেকে user পাওয়া যাবে
        
        print("Authenticated User:", user)  # Debugging এর জন্য user print করুন

        if not isinstance(user, CustomUser):  # User validation check
            return Response({"error": "User not found"}, status=400)

        return Response({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        })
