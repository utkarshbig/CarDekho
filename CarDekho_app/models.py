from django.db import models

# Create your models here.
class CarList(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=False)