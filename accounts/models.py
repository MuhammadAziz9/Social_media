from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='account_images/',default='images/images.jpg')

    def __str__(self):
        return self.username

