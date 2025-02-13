from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Comment,Like,Share,Save,Friendship
from django.http import HttpResponse
from django.db import models
from accounts.models import CustomUser
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('created_at')
    context = {
        'posts':posts
    }
    return render(request,'home.html',context)

from django.http import JsonResponse

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()
    else:
        Like.objects.create(user=request.user, post=post)


    return redirect('home')

@login_required
def toggle_friend(request, user_id):
    other_user = get_object_or_404(CustomUser, id=user_id)
    
    if request.user != other_user:
        friendship = Friendship.objects.filter(
            (models.Q(user1=request.user, user2=other_user) | models.Q(user1=other_user, user2=request.user))
        )

        if friendship.exists():
            friendship.delete()
        else:
            Friendship.objects.create(user1=request.user, user2=other_user)

    return redirect('home')




