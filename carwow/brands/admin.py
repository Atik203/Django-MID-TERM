from django.contrib import admin

# Register your models here.
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Brand, BrandAdmin)
