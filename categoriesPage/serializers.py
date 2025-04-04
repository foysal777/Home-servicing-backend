from rest_framework import serializers
from .models import Category, Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'details', 'price', 'location', 'image']

class CategorySerializer(serializers.ModelSerializer):
    listings = ListingSerializer(many=True) 

    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'listings'] 


