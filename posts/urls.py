from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('like/<int:post_id>/',views.toggle_like,name='toggle_like'),
    path('post/<int:post_id>/',views.post_detail,name='post_detail'),
    path('post/<int:post_id>/share',views.toggle_share,name='share_post'),
    path('post/<int:post_id>/save',views.toggle_save,name='toggle_save'),
    path('saved-post/',views.saved_post,name='saved_post'),
    path('delete-saved-post/<int:saved_post_id>/',views.delete_saved_post,name='delete_saved_post'),
    path('add_post/',views.add_post,name='add_post'),
    path('liked-post/',views.liked_post,name='liked_post'),
    path('profile<str:username>/',views.profile,name='profile'),
    path('delete-post/<int:post_id>/',views.delete_post,name='delete_post'),
    path('edit_post/<int:post_id>/',views.edit_post,name='edit_post'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('edit-comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),


]