from django.urls import path
from . import views

urlpatterns = [
    path('create-book', views.creatBook, name='creatBook'),

    path("listbook/", views.listBook, name='listbook'),

    path("author/", views.Create_Author, name='author'),
    path('details/<int:book_id>/', views.detailsView, name='details'),

    path('update/<int:book_id>/', views.updateBook, name='update'),

    path('delete/<int:book_id>/', views.deleteView, name='delete'),

    path('index/', views.index),

    path('search/', views.Search_Book, name='search'),

    path("", views.Register_user, name='register'),

    path('login/', views.LoginUser, name='login'),

    path('logout/', views.logOut, name='logout')

    

    


]
