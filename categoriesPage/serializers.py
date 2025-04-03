from rest_framework import serializers
from .models import Category, Listing, Order

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['title', 'details', 'price', 'location', 'image']

class CategorySerializer(serializers.ModelSerializer):
    listings = ListingSerializer(many=True)  # Include listings for each category

    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'listings']  # Include slug in the fields


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'listing', 'total_price', 'payment_status', 'transaction_id']