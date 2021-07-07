from django.urls import path 
from .api import mini_super, mini_super_detail

urlpatterns = [
    path('api/', mini_super),
    path('api/<int:pk>', mini_super_detail),
]