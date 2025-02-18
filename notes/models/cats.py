from django.db import models
from django.contrib.auth.models import User
from faker import Faker
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

