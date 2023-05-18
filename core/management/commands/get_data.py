from django.core.management.base import BaseCommand

from core.tasks import checking_currency


class Command(BaseCommand):
    help = "Загружает исторические датафреймы валюты с MT5"

    def handle(self, *args, **options):
        checking_currency()

