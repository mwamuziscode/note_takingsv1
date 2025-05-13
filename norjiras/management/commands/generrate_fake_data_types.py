from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from norjiras.models.project_models import Category, Project, Issue, IssueType
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake Categories, Issue, IssueType, and Projects for testing.'

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write("🔧 Generating fake data...")

        # Create Categories
        issuetype = []
        for _ in range(10):
            name = fake.unique.word().capitalize()
            issuetypes = IssueType.objects.create(
                name=name,
                slug=fake.sentence(),
                icon = fake.image_url()
            )
            issuetype.append(issuetypes)
        self.stdout.write("✅ IssueType Created.")
        self.stdout.write(self.style.SUCCESS("🎉 Done generating fake data."))
