from django.db import models
from django.contrib.auth.models import User
from faker import Faker
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
