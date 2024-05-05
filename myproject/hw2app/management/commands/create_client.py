from django.core.management.base import BaseCommand
from hw2app.models import Client


class Command(BaseCommand):
    help = "Create clients"

    def handle(self, *args, **kwargs):
        # client = Client(name='Jack', email='neo@example.com', phone='+7-777-777-77-77', address='Москва')
        # client = Client(name='Fil', email='fil@example.com', phone='+7-777-777-77-55', address='Москва')
        # client = Client(name='Sam', email='sam@example.com', phone='+7-777-777-77-44', address='Москва')
        # client = Client(name='Pit', email='pit@example.com', phone='+7-777-777-77-33', address='Москва')
        client = Client(name='Mary', email='mary@example.com', phone='+7-777-777-77-22', address='Москва')
        client.save()
        self.stdout.write(f'{client}')
