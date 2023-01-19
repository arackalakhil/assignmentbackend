
from django.conf import settings
from django.urls import include, path
from accounts.views import *
from rest_framework import routers

from . views import  RegisterUser
urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('profile',Profile.as_view()),
    path('task',UserTask.as_view()),
    path('apps',Showapp.as_view()),
    path('completetask',Completetask.as_view()),
    path('newapp',Addapp.as_view()),  
    path('myapps',Adminapps.as_view()),  

]