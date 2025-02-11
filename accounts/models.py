from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='account_images/')

    def __str__(self):
        return self.username

