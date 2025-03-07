# serializers.py
from rest_framework import serializers
from authentications.models import CustomUser  # Ensure CustomUser is imported

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        # Check if passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        # Optionally add more password validation here (length, special characters, etc.)
        return data

    def create(self, validated_data):
        # Create the user using the custom manager
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = False  # Set the user as inactive until email verification
        user.save()
        return user
