from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  phone_number_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. From 10 to 17 digits allowed.")
  phone_number = models.CharField(validators=[phone_number_regex], max_length=17, blank=True)
  location = models.CharField(max_length=100, blank=True)
  address = models.CharField(max_length=500, blank=True)
  birth_date = models.DateField(null=True, blank=True)