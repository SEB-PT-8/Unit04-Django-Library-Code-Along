from django.shortcuts import render

# Create your views here.

# 1. create a view function
# 2. add the function to the urls.py
# 3. create the template

# first parameter in all views is request
def homepage(request):
    return render(request,'homepage.html')


def about(request):
    return render(request, 'about.html')