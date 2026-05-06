from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm

# Create your views here.

# 1. create a view function
# 2. add the function to the urls.py
# 3. create the template

# first parameter in all views is request
def homepage(request):
    fruits = [{
        'name':'Apple'
        },
        {
            'name':'Orange'
        }
    ]
    return render(request,'homepage.html',{'fruits':fruits, 'is_logged_in':False})


def about(request):
    return render(request, 'about.html')

def author_list(request):
    all_authors = Author.objects.all()
    return render(request,'authors/author-list.html',{'authors':all_authors})


def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(request,'authors/author-details.html',{'author':author})


def delete_author(request, id):
    author = Author.objects.get(id = id)
    author.delete()
    return redirect('/authors')


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST) # request.POST same as request.body
        if form.is_valid():
            form.save()
            return redirect('/authors')
        # POST request logic
    form = AuthorForm()
    return render(request,'authors/author-form.html',{'form':form})



def author_update(request,id):
    author = Author.objects.get(id = id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author) # request.POST same as request.body
        if form.is_valid():
            form.save()
            return redirect('/authors')
        # POST request logic
    form = AuthorForm(instance=author)
    return render(request,'authors/author-form.html',{'form':form})
