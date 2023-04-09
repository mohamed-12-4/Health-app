from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
   blood_type = models.CharField(max_length=10)
   history = models.TextField()



