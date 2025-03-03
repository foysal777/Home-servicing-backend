from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title