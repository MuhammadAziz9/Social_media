from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='account_images/',default='images/images.jpg')

    def __str__(self):
        return self.username
    
class FriendShip(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='friends')
    friend = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='friend_of')
    created_at = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('user','friend')

    def __str__(self):
        return f"{self.user.username} followed {self.friend.username}"
    


