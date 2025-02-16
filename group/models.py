from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='owned_group')
    image = models.ImageField(upload_to='group_images',default='images/images.jpg')

    def __str__(self):
        return self.name
    
class GroupMember(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    joined_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','group')

    def __str__(self):
        return self.group
    
class GroupMessage(models.Model):
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} texted {self.text}"