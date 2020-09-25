from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('about',views.about,name='About'),
    path('contact',views.contact,name='Contact'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('signup',views.signup,name='signup'),


]
