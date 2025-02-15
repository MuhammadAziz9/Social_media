from django.shortcuts import render,redirect
from .models import Group,GroupMember
from.forms import GroupForm

# Create your views here.

def group_list(request):
    groups = Group.objects.all()
    context = {
        'groups':groups
    }
    return render(request,'group/groups.html',context=context)

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST,request.FILES)
        if form.is_valid():
            group=form.save(commit=False)
            group.admin=request.user
            group.save()
            GroupMember.objects.create(group=group,user=request.user)
            return redirect('group_list')
    else:
        form = GroupForm()
    context = {
        'form':form,
    }
    return render(request,'group/create_group.html',context=context)
