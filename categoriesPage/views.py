from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category,Order,Listing
from .serializers import CategorySerializer,OrderSerializer

from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal



@api_view(["GET"])
def category_detail(request, category_slug): 
    category = get_object_or_404(Category, slug=category_slug)  
    serializer = CategorySerializer(category)
    return Response(serializer.data)



# ******************************* SSL PAYMENT GATEWAY **********************

class InitiatePaymentView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            
            store_id = settings.SSLCOMMERZ_STORE_ID
            store_pass = settings.SSLCOMMERZ_STORE_PASS
            sslc_session = SSLCSession(store_id=store_id, store_pass=store_pass, is_live=False)
            
            payment_url = "http://127.0.0.1:8000/payment/success/"
            fail_url = "http://127.0.0.1:8000/payment/fail/"
            
            sslc_session.set_urls(success_url=payment_url, fail_url=fail_url, cancel_url=fail_url, ipn_url=payment_url)
            sslc_session.set_product_integration(total_amount=Decimal(order.total_price), currency='BDT', product_category='Services', product_name=order.listing.title, num_of_item=1, shipping_method='NO', product_profile='general')
            
            sslc_session.set_customer_info(name=order.user.username, email=order.user.email, address1='N/A', city='Dhaka', postcode='1207', country='Bangladesh', phone='017XXXXXXXX')
            
            response = sslc_session.init_payment()
            return Response({'payment_url': response['GatewayPageURL']}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentSuccessView(APIView):
    def post(self, request):
        tran_id = request.data.get('tran_id')
        order = get_object_or_404(Order, transaction_id=tran_id)
        order.payment_status = 'Completed'
        order.save()
        return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)

class PaymentFailView(APIView):
    def post(self, request):
        tran_id = request.data.get('tran_id')
        order = get_object_or_404(Order, transaction_id=tran_id)
        order.payment_status = 'Failed'
        order.save()
        return Response({'message': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)
