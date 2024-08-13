from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CustomUser

def create_user(username, password, email, is_instructor=False, **extra_fields):
    user = User.objects.create_user(username=username, password=password, email=email, **extra_fields)
    custom_user = CustomUser.objects.create(user=user, is_instructor=is_instructor)
    return user, custom_user

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pwd')  # Changed to match the form field name
        is_instructor = request.POST.get('is_instructor') == "on" 
        
        user, custom_user = create_user(username, password, email, is_instructor=is_instructor)
        
        return redirect('welcome_text')  # Corrected redirect syntax
    
    return render(request, 'register.html')  # Added to handle GET requests

def welcome_text(request):
    return render(request, 'welcome.html')
