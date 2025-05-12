from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify




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
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    

    # make project_key unique and auto-generated
    def save(self, *args, **kwargs):
        if not self.project_key:
            self.project_key = f"{str(self.name[:3].upper())}{str(self.pk)}{str(self.name[-2:].upper())}"
        super().save(*args, **kwargs)


    # slugify the project name to create a unique project key

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    

class IssueType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.ImageField(upload_to='issue_type_icons/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    issue_type = models.ForeignKey(IssueType, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.issue_type}] {self.title}"

















        


    

