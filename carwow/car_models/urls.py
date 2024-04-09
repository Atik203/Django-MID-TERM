
from django.urls import path

from .views import CarDetailView, buy_car

urlpatterns = [
    path('details/<int:id>/',CarDetailView.as_view(), name='car_detail'),
    path('buy/<int:id>/',buy_car, name='buy_car'),
]
