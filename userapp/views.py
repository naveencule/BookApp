

from django.shortcuts import render, get_object_or_404,redirect
from bookapp.models import Book
from .models import Cart,CartItem

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_details.html', {'book': book})

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'list_books.html', {'books': books, 'query': query})


def add_to_cart(request,book_id):
    book=Book.objects.get(id=book_id)

    if book.quantity>=0:
        cart,created=Cart.objects.get_or_create(user=request.user)
        cart_item,item_created=CartItem.objects.get_or_create(cart=cart,book=book)

        if not item_created:

            cart_item.quantity+=1
            cart_item.save()

        return redirect('addtocart')
    
def viewcart(request):
    cart,crated=Cart.objects.get_or_create(user=request.user)

    cart_items=cart.cartitem_set.all()
    cart_item=CartItem.objects.all()

    total_price=sum(item.book.price * item.quantity for item in cart_items)

    total_items=cart_items.count()

    context={'cart_items':cart_items,'cart_item':cart_item,'total_price':total_price,'total_items':total_items}
    
    return render (request,'cart.html',context)

def increase_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)

    if cart_item.quantity < cart_item.book.quantity:

        cart_item.quantity +=1
        cart_item.save()

    return redirect('addtocart')

def decrease_quantity(request,item_id):

    cart_item=CartItem.objects.get(id=item_id)

    if cart_item.quantity >1:

        cart_item.quantity -=1
        cart_item.save()

    return redirect('addtocart')

def remove_from_cart(request,item_id):
        
        try:

            cart_item=CartItem.objects.get(id=item_id)
            cart_item.delete()

        except cart_item.DoesNotExist:
            pass

        return redirect('addtocart')

   

        

    

