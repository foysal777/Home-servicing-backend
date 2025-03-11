from rest_framework import serializers
from .models import Category, Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['title', 'details', 'price', 'location', 'image']

class CategorySerializer(serializers.ModelSerializer):
    listings = ListingSerializer(many=True)  # Include listings for each category

    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'listings']  # Include slug in the fields
