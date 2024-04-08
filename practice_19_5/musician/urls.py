from django.urls import path

from .views import AddMusicianView, DeleteMusicianView, EditMusicianView

urlpatterns = [
    path('add_musician/', AddMusicianView.as_view(), name='add_musician'),
    path('edit_musician/<int:id>/', EditMusicianView.as_view(), name='edit_musician'),
    path('delete_musician/<int:id>/', DeleteMusicianView.as_view(), name='delete_musician'),
]


