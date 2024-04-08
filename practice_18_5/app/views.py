from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       SetPasswordForm)
from django.shortcuts import redirect, render

from .forms import EditProfileForm, RegistrationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            return redirect('login')
        else:
            messages.warning(request, 'Invalid input')
    else:
        form = RegistrationForm()    
    return render(request, 'RegistrationForm.html', {'form': form})

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                messages.success(request, 'You have been logged in successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()        
    return render(request, 'LoginForm.html', {'form': form})

def Logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')

@login_required
def pass_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            messages.success(request, 'Password changed successfully')
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            messages.warning(request, 'Invalid input')
    else:
        form = PasswordChangeForm(request.user)        
    return render(request, 'passChange.html', {'form': form})

@login_required
def pass_set(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            messages.success(request, 'Password set successfully')
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            messages.warning(request, 'Invalid input')
    else:
        form = SetPasswordForm(request.user)        
    return render(request, 'passChange.html', {'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Profile updated successfully')
            form.save()
            return redirect('profile')
        else:
            messages.warning(request, 'Invalid input')
    else:
        form = EditProfileForm(instance=request.user)        
    return render(request, 'profile.html', {'form': form})