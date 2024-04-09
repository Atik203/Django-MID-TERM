from django.contrib import admin

# Register your models here.
from .models import CarModel, Comment, Order

admin.site.register(CarModel)
admin.site.register(Order)
admin.site.register(Comment)
