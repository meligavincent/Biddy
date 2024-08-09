from django.urls import path , include

from .views import book_table,MenuView

urlpatterns = [
   
    path('', MenuView.as_view(), name='menu'),
    path('book_table/', book_table, name='book_table'),
]
