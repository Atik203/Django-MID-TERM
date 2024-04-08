from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import AlbumForm
from .models import Album

# class based views

class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'


class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'      
  