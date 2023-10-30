"""
Main View
"""

# MAKE NECESSARY IMPORTS
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes  # instead of force_text
from django.utils.http import urlsafe_base64_encode

def home(request):
    """
    This is the Main page.
    """


    return HttpResponse('')
