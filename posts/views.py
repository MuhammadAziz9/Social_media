from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Comment,Like,Share,Save
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('created_at')
    context = {
        'posts':posts
    }
    return render(request,'home.html',context)

@login_required



@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()
    else:
        Like.objects.create(user=request.user, post=post)


    return redirect('home')

def toggle_share(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    Share.objects.create(post=post,user=request.user)
    return redirect('home')

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

def toggle_save(request,post_id):
    post =get_object_or_404(Post,id=post_id)
    saved_post,created = Save.objects.get_or_create(user=request.user,post=post)

    if not created:
        saved_post.delete()
    
    return redirect('home')

def saved_post(request):
    saved_posts = Save.objects.filter(user=request.user).select_related('post')
    context = {
        'saved_posts':saved_posts
    }
    return render(request,'saved_post.html',context=context)

def delete_saved_post(request,saved_post_id):
    saved_post = get_object_or_404(Save,id=saved_post_id,user=request.user)
    saved_post.delete()
    return redirect('saved_post')





