"""
url.py
"""
from django.urls import path
from .views import db_connect, create_database, show_all_databases

urlpatterns = [
    path('', db_connect),
    path('create/', create_database),
    path('show_all_databases/', show_all_databases),
]
