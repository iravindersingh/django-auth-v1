
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.user_login, name='login'),
    path('signup/', views.register_view, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
