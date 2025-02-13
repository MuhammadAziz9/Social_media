from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Comment,Like,Share,Save,Friendship
from django.http import HttpResponse
from django.db import models
from accounts.models import CustomUser
from .forms import CommentForm
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


    return redirect('post_detail',post_id=post.id)

def toggle_share(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    Share.objects.create(post=post,user=request.user)
    return redirect('post_detail',post_id=post.id)

def post_detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail',post_id=post.id)
    else:
        form = CommentForm()
    context = {
        'comments':comments,
        'form':form,
        'post':post
    }
    return render(request,'post_detail.html',context)




