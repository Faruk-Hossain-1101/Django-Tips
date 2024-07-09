from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="Simple cron jobs"
    
    def handle(self, *args, **options):
        self.stdout.write("Hello from custom command!")