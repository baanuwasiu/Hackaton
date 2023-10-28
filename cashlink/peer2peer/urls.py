"""
Urls for the main portal.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='portal'),
]
