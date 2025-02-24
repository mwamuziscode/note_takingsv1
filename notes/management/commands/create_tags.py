from django.core.management.base import BaseCommand
from notes.views.utlilities import createTag  # Assuming your function is in `myapp.py`

class Command(BaseCommand):
    help = 'Creates all tags'

    def handle(self, *args, **kwargs):
        createTag()  # Call the function to create tags
        self.stdout.write(self.style.SUCCESS('Successfully created all tags'))
