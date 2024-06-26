from django.contrib import admin
from django.urls import path
from account.views import *

app_name='account'
urlpatterns = [
    path('register/',register,name='Register'),
    path('login/',login_view,name='Login'),
    path('logout/',logout_view,name='logout'),
]