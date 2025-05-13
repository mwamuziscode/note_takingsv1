from django.db import models
from norjiras.models.project_models import Project, IssueType


# create the summary models
class Summary(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='summary')
    #summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dues_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.project.name + ' - ' + self.summary[:20]  # Return the first 20 characters of the summary