from django.urls import path
from .views import category_detail

urlpatterns = [
    path("api/category/<str:category_slug>/", category_detail, name="category-detail"),  # Updated URL
]
