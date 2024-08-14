from django.urls import path
from . import views

urlpatterns = [

    path('list/', views.list_books, name='list_books'),
    path('details/<int:book_id>/', views.book_details, name='book_details'),
    path('search/', views.search_books, name='search_books'),
  
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='addtocart'),
    path('views-cart/', views.viewcart, name='viewscart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_qunatity'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
]
