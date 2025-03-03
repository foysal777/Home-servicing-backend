from django.urls import path
from .views import ServiceListCreateAPIView, ServiceDeleteAPIView

urlpatterns = [
    path('api/services/', ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('api/service-delete/<int:pk>/', ServiceDeleteAPIView.as_view(), name='service-delete'),
]
