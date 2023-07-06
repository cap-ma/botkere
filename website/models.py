from django.db import models


# Create your models here.
class Order(models.Model):
    phone_number = models.CharField(max_length=13)
    comment = models.CharField(max_length=100, null=True)
