from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Listing
from .serializers import CategorySerializer
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status

from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework import status

import stripe
from django.conf import settings
from .models import Listing

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(["GET"])
def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


# Stripe 
class CreateCheckoutSessionView(APIView):
    def post(self, request):
        try:
            listing_id = request.data.get("listing_id")
            if not listing_id:
                return Response({"error": "listing_id is required"}, status=400)

            listing = Listing.objects.get(id=listing_id)

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': listing.title,
                            'images': [listing.image] if listing.image else [],
                        },
                        'unit_amount': int(float(listing.price) * 100),  # price in pence
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:3000/success',
                cancel_url='http://localhost:3000/cancel',
            )

            return Response({'id': session.id}, status=200)

        except Listing.DoesNotExist:
            return Response({"error": "Listing not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
        
        

