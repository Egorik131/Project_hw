from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    # context = {'firstname': "egor", 'lastname': "Mel", 'age': 43}
    return render(request, 'hwapp/index.html')


def about(request):
    logger.info('About page accessed')
    return render(request, 'hwapp/about.html')