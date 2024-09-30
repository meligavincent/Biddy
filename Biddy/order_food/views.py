from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect,HttpResponse
from .models import BookTable
from .forms import BookTableForm
from .models import Food,Category
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Food
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('user saved')
            login(request, user)  # Connecte automatiquement l'utilisateur après l'inscription
            return redirect('home')  # Redirige vers la page d'accueil après l'inscription
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookTableForm(request.POST)
        print('La table a été reservée')
        if form.is_valid():
            form.save()
            print('La table a été reservée')
            return redirect('book_table_success')  # Create a success page or redirect back to home
    else:
        form = BookTableForm()
    return render(request, 'order_food/book.html', {'form': form})

@login_required(login_url='/accounts/login/')  # Redirect to login page if not logged in
def add_to_cart(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, food=food)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    #return HttpResponse(f"{food.name} has been added to your cart.")
    return redirect('cart_detail')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'order_food/cart_detail.html', {'cart': cart})

class MenuView(LoginRequiredMixin,View):
    template_name = "order_food/menu.html"

    def get(self, request, *args, **kwargs):
        foods = Food.objects.all()
        categories = Category.objects.all()
        context = {
            'foods': foods,
            'categories': categories,
        }
        return render(request, self.template_name, context)
    



class HomeView(LoginRequiredMixin, View):
    template_name = "order_food/index.html"
    login_url = '/accounts/login/'  # Specify the login URL
    redirect_field_name = 'redirect_to'  # Optional, defines the query param for redirection

    def get(self, request, *args, **kwargs):
        foods = Food.objects.all()
        categories = Category.objects.all()
        context = {
            'foods': foods,
            'categories': categories,
        }
        return render(request, self.template_name, context)
