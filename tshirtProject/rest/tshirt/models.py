from django.db import models



class Tshirt(models.Model):
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=10)

# Create your models here.
