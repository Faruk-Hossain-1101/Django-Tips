from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="Simple Custom Commands"
    
    def handle(self, *args, **options):
        self.stdout.write("Hello from custom command!")