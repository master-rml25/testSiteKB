from django.urls import path, include
from . import My_views
from django.contrib.auth import views

urlpatterns = [
    path('', My_views.index, name='home'),
    path('about', My_views.about, name='about'),
    path('login', views.LoginView.as_view(), name='login'),
    path('accounts', include('django.contrib.auth.urls')),
    path('blank_1', My_views.blank_1, name='blank_1'),
]
