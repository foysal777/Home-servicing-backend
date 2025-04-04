from django.urls import path
from .views import category_detail, CreateCheckoutSessionView

urlpatterns = [
    path("api/category/<str:category_slug>/", category_detail,
         name="category-detail"),  # Updated URL

    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

]
