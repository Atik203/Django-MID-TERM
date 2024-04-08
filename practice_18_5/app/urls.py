from django.urls import path

from .views import Login, Logout, pass_change, pass_set, profile, register

urlpatterns = [
   path('register/', register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('pass_change/', pass_change, name='pass_change'),
    path('profile/', profile, name='profile'),
    path('set_password/', pass_set, name='pass_change2')
]
