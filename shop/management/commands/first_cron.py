from django.core.management.base import BaseCommand
import logging
import datetime
logger = logging.getLogger('shop')


class Command(BaseCommand):
    help = 'Manage cron jobs'

    def handle(self, *args, **options):
        logger.info("Cron running at :: %s", datetime.datetime.now())