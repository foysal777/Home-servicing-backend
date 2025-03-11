from django.db import models

class Service(models.Model):
    category = models.CharField(max_length=255 ,default="General")  
    title = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(default=1)
    location = models.CharField(max_length=255, blank=True, null=True)  # Added location field

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
