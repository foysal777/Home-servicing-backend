
from django.contrib.auth import authenticate
from rest_framework import serializers
from authentications.models import CustomUser  

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser  
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        # Check if passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")

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


# for log in (admin log in korle)
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        # Check if user exists with given email
        user = authenticate(username=email, password=password)
        
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

    #  return super & staff user 
        return {
            "user": user,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
        }