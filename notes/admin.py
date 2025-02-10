from django.contrib import admin

# Register your models here.
from notes.models import Category, Tag, Note

admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Tag)