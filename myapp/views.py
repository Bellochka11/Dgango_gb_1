#представления классы или функции для логики url как реагировать на запрос пользователя
from django.shortcuts import render #отрисовка шаблона
from django.http import HttpResponse #класс возвращает ответ от сервера к клиенту
import logging 
 
logger = logging.getLogger(__name__) 
 
def index(request): #request - запрос который отправляет пользователь
    logger.info('Index page accessed') 
    return HttpResponse("Hello, world!") 
 
def about(request): 
    try: 
        # print('la')
        # some code that might raise an exception 
        result = 1 / 0 
    except Exception as e: 
        logger.exception(f'Error in about page: {e}') 
        return HttpResponse("Oops, something went wrong.") 
    else: 
        logger.debug('About page accessed') 
        return HttpResponse("This is the about page.") 