from django.shortcuts import render

from brands.models import Brand
from car_models.models import CarModel


def home(request, brand_slug=None):
    cars = CarModel.objects.all()
    if brand_slug:
        cars = cars.filter(brand__slug=brand_slug)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brands': brands})