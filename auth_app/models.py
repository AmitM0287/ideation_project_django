from django.db import models


# User model
class User(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    property = models.CharField(max_length=60)
    service = models.CharField(max_length=60)
    message = models.CharField(max_length=150)
    date_joined = models.DateTimeField(auto_now_add=True)
