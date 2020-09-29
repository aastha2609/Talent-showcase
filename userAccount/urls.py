from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.userHome,name='userHome'),
    path('post',views.post,name='post'),
    path('userpost',views.userpost,name='userpost'),
    path('like_disklike',views.likepost, name='like_dislike_post'),
    path('<int:ID>',views.delPost,name='delpost'),
    path('<str:username>',views.userProfile,name='userprofile')
]
 