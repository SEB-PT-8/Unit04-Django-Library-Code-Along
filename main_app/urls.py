from django.urls import path
from . import views


urlpatterns = [
   path('home/', views.homepage ),
   path('about/', views.about ),
   path('authors/', views.author_list ),
   path('authors/<int:id>', views.author_details ),
   path('authors/delete/<int:id>', views.delete_author ),
   path('authors/create/', views.author_create ),
   path('authors/<int:id>/update/', views.author_update ),

]
