from django.urls import path

from .views import (EditProfileView, UserLoginView, UserLogoutView,
                    UserRegisterView, profile)

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile')
]
