from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_best_seller = models.BooleanField()
    birth_date = models.DateField(null=True)