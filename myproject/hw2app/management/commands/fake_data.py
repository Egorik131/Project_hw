from django.core.management.base import BaseCommand
from hw2app.models import Product, Order, Client


class Command(BaseCommand):
    help = "Generate fake products and orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'name{i}@example.com', phone='+7-777-777-77-22', address=f'Сity{i}')
            client.save()
            for j in range(1, count + 1):
                product = Product(name=f'Name{j}', description=f'description{j}', price=j * 3, quantity=j)
                product.save()
                for k in range(1, count + 1):
                    order = Order(
                        customer=client,
                        product=product,
                        total_price=k,
                    )
                    order.save()
