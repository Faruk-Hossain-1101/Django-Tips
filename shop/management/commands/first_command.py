from django.core.management.base import BaseCommand
import logging


logger = logging.getLogger('shop')
class Command(BaseCommand):
    help="Simple Custom Commands"
    
    def handle(self, *args, **options):
        logger.info("Hello World!")
        self.stdout.write("Hello from custom command!")