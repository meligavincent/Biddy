from django.urls import path , include

from .views import book_table,MenuView,HomeView

urlpatterns = [
   
    path('menu/', MenuView.as_view(), name='menu'),
    path('', HomeView.as_view(), name='home'),

    path('book_table/', book_table, name='book_table'),
]
