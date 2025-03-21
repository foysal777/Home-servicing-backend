from django.urls import path
from .views import (
    post_list_create,
    post_detail,
    CommentAPIView,
   

    
)

urlpatterns = [
    # Post Endpoints
    path('posts/', post_list_create, name='post-list-create'),  # GET, POST
    path('posts/<int:post_id>/', post_detail, name='post-detail'),  # GET, PUT, DELETE
    
    # Comment Endpoints
    path('posts/<int:post_id>/comments/', CommentAPIView.as_view(), name='comment-list-create'),

]
