from django import forms
from .models import BookTable
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = ['name', 'email', 'phone', 'date', 'time', 'number_of_people']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
