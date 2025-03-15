from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  # Authentication Required

    def get(self, request):
        user = request.user  # JWT থেকে user নেওয়া হবে

        print("🚀 Debug: Authenticated User ->", user)  # Debugging

        if user.is_anonymous:  # যদি AnonymousUser হয়
            return Response({"error": "Invalid Token or User not authenticated"}, status=401)

        return Response({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        })
