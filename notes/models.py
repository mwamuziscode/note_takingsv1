from django.db import models
from django.contrib.auth.models import User
from faker import Faker

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    #picture = models.ImageField(upload_to='notes/', null=True, blank=True, default='notes/default.jpg') 
    picture = models.URLField(max_length=255, null=True, blank=True, default='https://via.placeholder.com/150')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_archived = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    # get img url or upload image
    def get_picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return self.picture
        
