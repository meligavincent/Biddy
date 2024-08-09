from django import forms
from .models import BookTable

class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = ['name', 'email', 'phone', 'date', 'time', 'number_of_people']
