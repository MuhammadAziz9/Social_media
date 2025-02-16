from django.urls import path
from . import views

urlpatterns = [
    path('group_list/',views.group_list,name='group_list'),
    path('group_detail/<int:group_id>/',views.group_detail,name='group_detail'),
    path('create_group/',views.create_group,name='create_group'),
    path('join/<int:group_id>/',views.join_group,name='join_group'),
    path('leave/<int:group_id>/',views.leave_group,name='leave_group'),
]