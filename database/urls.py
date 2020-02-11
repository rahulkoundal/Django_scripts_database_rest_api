"""
url.py
"""
from django.urls import path
from .views import db_connect

urlpatterns = [
    path('', db_connect),
]
