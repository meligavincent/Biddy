from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect
from .models import BookTable
from .forms import BookTableForm
from .models import Food,Category
# Create your views here.

def book_table(request):
    if request.method == 'POST':
        form = BookTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_table_success')  # Create a success page or redirect back to home
    else:
        form = BookTableForm()
    return render(request, 'order_food/book.html', {'form': form})

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
    
