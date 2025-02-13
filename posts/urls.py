from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('like/<int:post_id>/',views.toggle_like,name='toggle_like'),
    path('post/<int:post_id>/',views.post_detail,name='post_detail'),
    path('post/<int:post_id>/share',views.toggle_share,name='share_post'),
]