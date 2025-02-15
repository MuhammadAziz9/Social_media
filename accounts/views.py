from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import FriendShip
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if 'image' in request.FILES:
                user.image = request.FILES['image']
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request,'registration/register.html',context)




