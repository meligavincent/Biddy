from django.urls import path , include

from .views import book_table,MenuView,HomeView,add_to_cart,cart_detail,signup,remove_from_cart

urlpatterns = [
   
    path('menu/', MenuView.as_view(), name='menu'),
    path('', HomeView.as_view(), name='home'),

    path('book_table/', book_table, name='book_table'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('accounts/signup/', signup, name='signup'),

]
