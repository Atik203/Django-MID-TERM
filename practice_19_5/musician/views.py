from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import MusicianForm
from .models import Musician


# Create your views here.
class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')


class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    
    
class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = 'delete_musician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'    
