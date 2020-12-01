from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    bid = models.IntegerField()
    desc = models.CharField(max_length=128)
    image = models.URLField(blank=True)
    time = models.DateTimeField()

class comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=128)

class bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.IntegerField()


