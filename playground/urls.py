from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('forgotPassword/', views.forgotPassword),
]