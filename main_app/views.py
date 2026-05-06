from django.shortcuts import render

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