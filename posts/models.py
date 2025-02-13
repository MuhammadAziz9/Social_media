from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=300,blank=True)
    image = models.ImageField(upload_to='post_files/',blank=True,null=True)
    video = models.FileField(upload_to='post_files/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()
    
    def total_shares(self):
        return self.shares.count()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.post}"

class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')

    class Meta:
        unique_together = ('user','post')

    def __str__(self):
        return f"{self.user.username} liked {self.post}"

class Share(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} shared {self.post}"

class Save(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} saved {self.post}" 
    


class Friendship(models.Model):
    user1 = models.ForeignKey(CustomUser, related_name="friends_1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(CustomUser, related_name="friends_2", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1} ↔ {self.user2}"

