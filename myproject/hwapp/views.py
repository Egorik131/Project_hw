from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    html = """
       <!doctype html>
           <html lang="ru">
           <head>
               <meta charset="utf-8">
               <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
               <link rel="icon" href="data:;base64,=">
               <title>Главная страница</title>
           </head>
           <body>
               <div class="container-fluid">
                   <ul class="nav nav-pills justify-content-end align-items-end">
                       <li class="nav-item"><a href="" class="nav-link">Главная страница</a></li>
                       <li class="nav-item"><a href="/about/" class="nav-link">О себе</a></li>
                       <li class="nav-item"><a href="/shop/" class="nav-link">Интернет магазин</a></li>
                   </ul>
                   <h1 class="heading">Главная страница</h1>
                   <h2 class="heading">Первый сайт на Django</h2>
                   <p> Это страница моего первого сайта на Django.</p>                    
               </div> 
               <div class="row fixed-bottom modal-footer">
                   <hr>
                   <p>Все права защищены &copy;</p>
               </div>
           </body>
           </html>
       """
    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    html = """
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <link rel="icon" href="data:;base64,=">
                <title>О себе</title>
            </head>
            <body>
                <div class="container-fluid">
                    <ul class="nav nav-pills justify-content-end align-items-end">
                        <li class="nav-item"><a href="/" class="nav-link">Главная страница</a></li>
                        <li class="nav-item"><a href="" class="nav-link">О себе</a></li>
                        <li class="nav-item"><a href="/shop/" class="nav-link">Интернет магазин</a></li>
                    </ul>
                <div class="top">
                    <h1 class="title">Мельниченко Егор</h1>
                </div>
                <div class="about">
                    <h2 class="heading">О себе</h2>
                    <p class="description">
                        Руководитель IT-компании. Люблю получать новые знания.<br>
                        Люблю путешествовать и заниматься активными видами спорта.
                    </p>
                </div>
                <div class="row fixed-bottom modal-footer">
                    <hr>
                    <p>Все права защищены &copy;</p>
                </div>
            </body>
            </html>
        """
    return HttpResponse(html)
