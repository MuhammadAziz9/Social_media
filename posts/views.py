from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Comment,Like,Share,Save
from .forms import CommentForm,PostForm
from django.http import HttpResponseRedirect
from accounts.models import CustomUser,FriendShip
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('created_at')
    context = {
        'posts':posts
    }
    return render(request,'home.html',context)

@login_required
def add_post(request):
    post = None
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {
        'form':form,
        'post':post
    }
    return render(request,'add_post.html',context)


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


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id  # Fikr tegishli bo‘lgan post ID sini olish

    if comment.user == request.user:
        comment.delete()
    
    return redirect('post_detail', post_id=post_id)  # post_detail sahifasiga qaytish

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        return redirect('post_detail', post_id=comment.post.id)  # Faqat egasi tahrirlashi mumkin

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})


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

def liked_post(request):
    liked_posts = Like.objects.filter(user=request.user).select_related('post')
    context = {
        'liked_posts':liked_posts
    }
    return render(request,'liked_post.html',context)

def profile(request,username):
    user = get_object_or_404(CustomUser,username=username)
    user_posts = Post.objects.filter(user=user).order_by('-created_at')
    is_friend = FriendShip.objects.filter(user=request.user, friend=user).exists()

    context = {
        'user_profile':user,
        'user_posts':user_posts,
        'is_friend':is_friend
    }
    return render(request,'profile.html',context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Faqat post egasi o‘chira olishi kerak
    if post.user == request.user:
        post.delete()
        return redirect('profile', username=request.user.username)  # Profil sahifasiga qaytish

    return redirect('home')

def edit_post(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile',username=request.user.username)
    else:
        form = PostForm(instance=post)
    context = {
        'form':form,
        'post':post
    }
    return render(request,'edit_post.html',context)

@login_required
def add_friend(request, username):
    friend = get_object_or_404(CustomUser, username=username)  # Username orqali foydalanuvchini olish

    # Do‘stlik mavjudligini tekshirish
    if not FriendShip.objects.filter(user=request.user, friend=friend).exists():
        FriendShip.objects.create(user=request.user, friend=friend)

    return redirect('profile', username=username)

@login_required
def remove_friend(request, username):
    friend = get_object_or_404(CustomUser, username=username)  # Username orqali foydalanuvchini olish

    # Agar do‘stlik mavjud bo‘lsa, o‘chirish
    FriendShip.objects.filter(user=request.user, friend=friend).delete()

    return redirect('profile', username=username)

def friends_view(request):
    friends = FriendShip.objects.filter(user=request.user)
    context = {
        'friends':friends
    }
    return render(request,'friends.html',context=context)




