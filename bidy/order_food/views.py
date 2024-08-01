from django.shortcuts import render
from django.views.generic import ListView

from .models import Food
# Create your views here.

class FoodListView(ListView):
    model = Food
