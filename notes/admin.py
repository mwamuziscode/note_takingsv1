from django.contrib import admin

# Register your models here.
from notes.models.cats import Category
from notes.models.notest import Note
from notes.models.tag import Tag
from notes.models.profiles import Profile

admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Profile)