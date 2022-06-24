from unicodedata import name
from django.db import models

class MangoShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)