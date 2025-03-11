from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer

@api_view(["GET"])
def category_detail(request, category_slug): 
    category = get_object_or_404(Category, slug=category_slug)  
    serializer = CategorySerializer(category)
    return Response(serializer.data)
