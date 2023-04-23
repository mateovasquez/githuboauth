from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  phone_number = models.CharField(max_length=9, blank=True)
  location = models.CharField(max_length=100, blank=True)
  address = models.CharField(max_length=500, blank=True)
  birth_date = models.DateField(null=True, blank=True)