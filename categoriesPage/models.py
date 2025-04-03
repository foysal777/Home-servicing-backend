from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Slug field
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:  # Slug field is empty
            self.slug = slugify(self.name)  # Auto generate slug from name
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return self.name

class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=255)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.title
    

class Order(models.Model):
    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='Pending')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.payment_status}"
