"""
Manaagement Panel view.
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
    This is the signin method.
    """
    context = {'sales': True}
    # if request.method == "POST":
    #
    #     username = request.POST['account_id'].upper()
    #     password = request.POST['account_password']
    #     user = authenticate(username=username, password=password)
    #
    #     if user is not None:
    #         login(request, user)
    #
    #         if user.username.upper().startswith("A"):
    #             # Send Token to User
    #             login_token_generator(request)
    #             return redirect('accounts_token')
    #
    #         else:
    #             messages.error(request, "You are not authorized here")
    #             logout(request)
    #             return redirect('accounts_signin')
    #
    #     else:
    #         messages.error(request, "Login failed, invalid credentials")
    #         return redirect('accounts_signin')

    return render(request, 'management/sales.html', context)
