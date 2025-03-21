from django.db import models
from django.conf import settings



# Blog Post Model
class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=200 ,default='Uncategorized')
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=500, blank=True, null=True) 

    def __str__(self):
        return self.title

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"