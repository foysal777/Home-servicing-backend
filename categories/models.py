from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=500)  
    listings = models.IntegerField(default=0)

    def __str__(self):
        return self.name
