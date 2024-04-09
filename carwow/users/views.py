from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from car_models.models import Order

from .forms import EditProfileForm, RegistrationForm


# class based registration view
class UserRegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'RegistrationForm.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid input')
        return super().form_invalid(form)
    
class UserLoginView(LoginView):
    template_name = 'LoginForm.html'

    def form_valid(self, form):
        messages.success(self.request, 'You have been logged in successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid username or password')
        return super().form_invalid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            messages.success(request, 'You have been logged out successfully')
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
            
@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid input')
        return super().form_invalid(form)
    
    def get_object(self):
        return self.request.user

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})