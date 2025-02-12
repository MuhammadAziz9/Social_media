from django.shortcuts import render
from .models import Post,Comment,Like,Share,Save
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('created_at')
    context = {
        'posts':posts
    }
    return render(request,'home.html',context)
