from django.contrib import admin

# Register your models here.
from notes.models.cats import Category
from notes.models.notes import Note
from notes.models.tag import Tag

admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Tag)