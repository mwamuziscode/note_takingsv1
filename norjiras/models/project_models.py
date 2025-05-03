from django.db import models
from django.contrib.auth.models import User
import faker
from faker import Faker



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    project_key = models.CharField(max_length=10, unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projiras')
    project_lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_lead')
    project_members = models.ManyToManyField(User, related_name='project_members', blank=True)
    project_status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    project_description = models.TextField(blank=True, null=True)
    project_urls = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    # make project_key unique and auto-generated
    def save(self, *args, **kwargs):
        if not self.project_key:
            self.project_key = f"{str(self.name[:3].upper())}{str(self.pk)}{str(self.name[-2:].upper())}"
        super().save(*args, **kwargs)



    # key mjust be uppercase and 10 characters lon

# create a project with fake data


















        


    

