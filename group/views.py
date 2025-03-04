from django.shortcuts import render,redirect,get_object_or_404
from .models import Group,GroupMember,GroupMessage
from.forms import GroupForm

# Create your views here.

def group_list(request):
    groups = Group.objects.all()
    context = {
        'groups':groups
    }
    return render(request,'group/groups.html',context=context)


def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    messages = GroupMessage.objects.filter(group=group).order_by('created_at')

    if request.method == "POST":
        text = request.POST.get("message-text")
        if text:
            GroupMessage.objects.create(group=group, sender=request.user, text=text)
            return redirect('group_detail', group_id=group.id)  # Yangi xabar qo‘shilgandan keyin sahifani qayta yuklash

    return render(request, 'group/group_detail.html', {'group': group, 'messages': messages})


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

def join_group(request,group_id):
    group = get_object_or_404(Group,id=group_id)
    if not GroupMember.objects.filter(user=request.user,group=group).exists():
        GroupMember.objects.create(group=group,user=request.user)
    return redirect('group_list')

def leave_group(request,group_id):
    group = get_object_or_404(Group,id=group_id)
    GroupMember.objects.filter(group=group,user=request.user).delete()
    return redirect('group_list')
