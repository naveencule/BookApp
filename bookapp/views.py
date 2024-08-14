from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .form import AuthorForm, BookForm
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout



def creatBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('creatBook')  # Redirect to the same view after saving
    else:
        form = BookForm()  # Create an empty form for GET requests

    books = Book.objects.all()  # Fetch all books to display in the table
    return render(request, 'text.html', {'form': form, 'books': books})


def Create_Author(request):

    if request.method=='POST':

        form=AuthorForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()


            return redirect('/')
        
    else:
        form=AuthorForm()

    return render(request,'author.html',{'form':form})
    

def listBook(request):
    books = Book.objects.all()

    paginator=Paginator(books,3)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:

        page=paginator.page(page_number.num_pages)


    return render(request, 'listbook.html', {'books': books, 'page':page})



def detailsView(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'detailsview.html', {'book': book})




def updateBook(request, book_id):

   #method used using forms

   book=Book.objects.get(id=book_id)
   if request.method=='POST':
       form=BookForm(request.POST,request.FILES,instance=book)

       if form.is_valid():
           form.save()

           return redirect('listbook/')
       
   else:
       form=BookForm(instance=book)

   return render(request,'updateview.html',{'form':form})


def deleteView(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('listbook')  
    return render(request, 'deleteview.html', {'book': book})

def index(request):

    return render (request,'index.html')


def Search_Book(request):

    query=None
    books=None

    if 'q' in request.GET:

        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))

    else:
        books=[]

    context={'books': books, 'query':query}

    return render(request,'search.html',context)

def Register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email ID already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                messages.success(request, 'User registered successfully. Please login.')
                return redirect('login')  # Redirect to login after registration
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'register.html')




def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('listbook')  # Redirect to listbook page after login
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')



def logOut(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')






        





