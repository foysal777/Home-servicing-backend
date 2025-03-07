
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('categories.urls') ),
    path('categoriesPage/', include('categoriesPage.urls') ),
    path('services/', include('services.urls') ),
    path('review/', include('review.urls') ),
    path('authentications/', include('authentications.urls') ),
   
    
]
