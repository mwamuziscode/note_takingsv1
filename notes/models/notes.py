from django.db import models
from django.contrib.auth.models import User
from faker import Faker
from ckeditor.fields import RichTextField
# RichTextUploadingField()  #
from ckeditor_uploader.fields import RichTextUploadingField

from .cats import Category
from .tag import Tag


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    # content = models.TextField()
    content = RichTextUploadingField()
    frontpic = models.ImageField(upload_to='notes/', null=True, default='notes/default.jpg')
    # picture = models.URLField(max_length=255, null=True, blank=True, default='https://via.placeholder.com/150')
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