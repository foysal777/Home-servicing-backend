from django.urls import path
from .views import UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), 
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),


]
