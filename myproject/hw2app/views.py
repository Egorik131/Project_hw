from django.shortcuts import render, get_object_or_404
import logging
from django.http import HttpResponse
from .models import Client, Order, Product
from django.utils import timezone

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'hw2app/index.html')


def all_orders(request, order_id):
    logger.info('About page accessed')
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'hw2app/orders_date.html', {'order': order})

def get_clients(request):
    clients = Client.objects.all()
    context = {'clients': clients, 'name': 'Клиенты'}
    return render(request, 'hw2app/all_clients.html', context)

def get_client_on_id(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    # client = Client.objects.filter(pk=client_id).first()
    if client is not None:
        context = {'client': client, 'client_id': f'Выбранный id клиента №: {client_id} '}
        return render(request, 'hw2app/clients.html', context)


def get_clients_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    # orders = Order.objects.filter(customer=client).order_by('-customer_id')
    orders = Order.objects.filter(customer=client).all()

    context = {'client': client, 'orders': orders}
    return render(request, 'hw2app/all_orders.html', context)


def get_orders_on_date(request, client_id, days):
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client, date_ordered__range=(start_date, end_date)).order_by('-date_ordered')
    context = {'client': client, 'orders': orders, 'days': days}
    return render(request, 'hw2app/orders_date.html', context)

