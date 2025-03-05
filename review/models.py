from django.db import models

class Review(models.Model):
    STAR_CHOICES = [
        ("★☆☆☆☆", "1 Star"),
        ("★★☆☆☆", "2 Stars"),
        ("★★★☆☆", "3 Stars"),
        ("★★★★☆", "4 Stars"),
        ("★★★★★", "5 Stars"),
    ]
    
    name = models.CharField(max_length=100)
    review_title = models.CharField(max_length=200)
    review_text = models.TextField()
    rating = models.CharField(max_length=5, choices=STAR_CHOICES, default="★★★★★")
    image = models.URLField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.review_title} - {self.rating}"
