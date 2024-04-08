from django.urls import path

from .views import AddAlbumView, DeleteAlbumView, EditAlbumView

urlpatterns = [
    path('add_album/', AddAlbumView.as_view(), name='add_album'),
    path('edit_album/<int:id>/', EditAlbumView.as_view(), name='edit_album'),
    path('delete_album/<int:id>/', DeleteAlbumView.as_view(), name='delete_album'),
]
