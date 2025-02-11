from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
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

