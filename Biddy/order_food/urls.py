from django.urls import path , include

from .views import FoodListView,CategoryListView,MenuView

urlpatterns = [
   
    path('', MenuView.as_view(), name='menu'),
]
