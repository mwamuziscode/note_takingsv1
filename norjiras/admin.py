from django.contrib import admin
from norjiras.models import  Project, Category, IssueType, Issue

 #Issue, Comment, Attachment, UserProfile



# Register your models here.
""" Admin interface for the Project model.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'Lead_by', 'project_urls', 'updated_at')
    search_fields = ('name', 'category__name', 'Lead_by')
    list_filter = ('category',)
    
    #ordering = ('-created_at',)
    #date_hierarchy = 'created_at'
    list_per_page = 10

    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'Lead_by', 'project_urls')
        }),
        ('Date Information', {
            'fields': ('updated_at'),
            'classes': ('collapse',)
        }),
    )
"""

admin.site.register(Project)
admin.site.register(Category)






@admin.register(IssueType)
class IssueTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'icon']

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'issue_type', 'created_at']
    list_filter = ['issue_type']

