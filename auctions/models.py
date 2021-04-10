from django.contrib.auth.models import AbstractUser
from django.db import models


class Listing(models.Model):
    username = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    bid = models.IntegerField()
    desc = models.CharField(max_length=1000)
    image = models.URLField(blank=True, null=True)
    time = models.DateTimeField()
    bid_user = models.CharField(max_length=64, null=True, blank=True)
    closed = models.BooleanField()


class User(AbstractUser):
    wishlist = models.ManyToManyField(Listing, null=True, blank=True)


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=128)


class Bid(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="listings")
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.IntegerField()
