
from django.contrib import admin
from django.urls import include, path

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
]
