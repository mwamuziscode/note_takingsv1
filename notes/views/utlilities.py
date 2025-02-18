

from notes.models import Note, Category, Tag
from faker import Faker
from django.contrib.auth.models import User





def createNote():
    fake = Faker()
    for _ in range(10):
        category = Category.objects.create(name=fake.word())
        tag = Tag.objects.create(name=fake.word())
        note = Note.objects.create(
            title=fake.sentence(),
            content=fake.text(),
            picture= "https://loremflickr.com/320/240",
            category=category,
            is_archived=fake.boolean(chance_of_getting_true=50),
            user= User.objects.filter(is_superuser=True).order_by('?').first()
        )
        note.tags.add(tag)
        note.save()
    return 'Fake data created successfully'

# createNote()


# DELETE ALL TAGS AND CATEGORIES
def DeleteAll(request):
   def deleteAllTags():
    Tag.objects.all().delete()
    return 'All Tags deleted successfully'

   def deleteAllCategories():
    Category.objects.all().delete()
    return 'All Categories deleted successfully'

   def deleteAllNotes():
    Note.objects.all().delete()
    return 'All Notes deleted successfully'

   deleteAllTags()
   deleteAllCategories()
   deleteAllNotes()

# DeleteAll()