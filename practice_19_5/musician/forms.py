from django import forms

from .models import Musician


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'instrument_type': 'Instrument Type',
            'email': 'Email',
            'phone': 'Phone Number'
        }