from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer

@api_view(["GET"])
def category_detail(request, category_name):
    category = get_object_or_404(Category, name__iexact=category_name)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
