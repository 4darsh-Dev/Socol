from django.contrib import admin
from django.urls import path,include
from home  import views

# test user passwords
# hriday ---> pass hraj@420

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name ='logout'),
    path('signup', views.signupHandle , name='signup')

    
    
]