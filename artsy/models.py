from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Art(models.Model):
    CATEGORY_CHOICES = [
        ('PAINT', 'Painting'),
        ('SCULP', 'Sculpture'),
        ('DIGIT', 'Digital Art'),
        ('SKETC', 'Sketch'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='art')
    item_name= models.CharField(max_length=120, null=True, blank=True)
    item_description = models.TextField(max_length=120)
    price = models.FloatField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='PAINT')
    image=models.ImageField(upload_to='art_images/', null=True, blank=True)

    def __str__(self):
        return self.item_name


class Bid(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder.username} bid {self.bid_amount} on {self.art.item_name}"

