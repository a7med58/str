from multiprocessing.dummy import active_children
from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm
# Create your views here.





def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
    
    
    context = {
        'category': Category.objects.all(),
        'dept': Dept.objects.all(),
        'status': Status.objects.all(),
        'books': Book.objects.order_by('-thidate'),
        


    }
    return render(request, 'pages/index.html', context)


def dash(request):
 
    
    context = {
        'allbooks': Book.objects.filter(action=True).count(),
        'stat': Book.objects.filter(stat = 1).count(),
        'statcans': Book.objects.filter(stat = 5).count(),
        'abt': Book.objects.filter(depart = 1).count(),
        'aag': Book.objects.filter(depart = 2).count(),
        'azn': Book.objects.filter(depart = 3).count(),
        'adr': Book.objects.filter(depart = 4).count(),
        'apm': Book.objects.filter(depart = 5).count(),
        'aoh': Book.objects.filter(depart = 6).count(),
        'agn': Book.objects.filter(depart = 7).count(),
        'aeg': Book.objects.filter(depart = 8).count(),
        'amb': Book.objects.filter(depart = 9 ).count(),
        'abc': Book.objects.filter(depart = 10).count(),
        'aft': Book.objects.filter(depart = 11).count(),
        'avc': Book.objects.filter(depart = 12).count(),
        'eep': Book.objects.filter(depart = 13).count(),
        'aap': Book.objects.filter(depart = 14).count(),
        'aec': Book.objects.filter(depart = 15).count(),
        'ass': Book.objects.filter(depart = 16).count(),
        'ase': Book.objects.filter(depart = 17).count(),
        'app': Book.objects.filter(depart = 18).count(),
        'dhp': Book.objects.filter(category = 6).count(),
        'mac': Book.objects.filter(category = 7).count(),

       



        'category': Category.objects.all(),
        'dept': Dept.objects.all(),
        'status': Status.objects.all(),
        'books': Book.objects.order_by('-thidate'),

      


    }
    return render(request, 'pages/dash.html', context)










def book(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    
    
    
    context = {
        'category': Category.objects.all(),
        'dept':Dept.objects.all(),
        'status': Status.objects.all(),
        'books':search,
        'books': Book.objects.order_by('-thidate'),

    

    }
    return render(request, 'pages/book.html', context)


def update(request,id):
    book_id = Book.objects.get(id=id) 
    if request.method == 'POST':
       book_save = BookForm(request.POST, request.FILES, instance=book_id)
       if  book_save.is_valid():
            book_save.save()
            return redirect('index')
    else:
            book.save = BookForm(instance=book_id)
    context = {
            'form': book.save,
        }
    return render(request, 'pages/update.html', context)




def delete(request , id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('index')
    return render(request, 'pages/delete.html')
