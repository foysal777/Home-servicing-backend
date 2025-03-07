from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)  # User is inactive until verification
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)  # Track verification status

    # Custom manager for the model
    objects = CustomUserManager()

    # Changing the USERNAME_FIELD to 'email' for authentication
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # Override the default related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Custom related_name to avoid conflict with auth.User
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Custom related_name to avoid conflict with auth.User
        blank=True
    )

    def __str__(self):
        return self.email


# email : fadmin@gmail.com 
# password : 888 