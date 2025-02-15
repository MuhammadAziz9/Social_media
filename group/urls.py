from django.urls import path
from . import views

urlpatterns = [
    path('group_list/',views.group_list,name='group_list'),
    path('create_group/',views.create_group,name='create_group')
]