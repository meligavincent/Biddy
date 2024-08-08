from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from .models import Food,Category
# Create your views here.

class FoodListView(ListView):
    template_name =  "order_food/menu.html"
    context_object_name = "foods"
    model = Food

class CategoryListView(ListView):
    template_name =  "order_food/menu.html"
    context_object_name = "categories"
    model = Category

class MenuView(View):
    template_name = "order_food/menu.html"

    def get(self, request, *args, **kwargs):
        foods = Food.objects.all()
        categories = Category.objects.all()
        context = {
            'foods': foods,
            'categories': categories,
        }
        return render(request, self.template_name, context)
    