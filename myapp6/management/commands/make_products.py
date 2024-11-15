from random import choice, randint, uniform #генерация случайных чисел

from django.core.management.base import BaseCommand
from myapp5.models import Category, Product

# (venv) PS C:\Users\BOSS\Desktop\Django_code\myproject> python .\manage.py make_products 10000
# создали в бд продукт 10000 продуктов
class Command(BaseCommand):
    help = "Generate fake products." #справка

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count') #добавляем кол во продуктов для генерации

    def handle(self, *args, **kwargs):
        categories = Category.objects.all() #извлекаем все категории
        products = [] #продукты которые хотим в будущем добавить в бд
        count = kwargs.get('count') #запрос к каунт который введет пользователь в командной строке кол во продуктов которые хоим сгенерировать
        for i in range(1, count + 1): #добавляем продукты
            products.append(Product(
                    name=f'продукт номер {i}',
                    category=choice(categories), #выбирает случайным обравзом категорию
                    description='длинное описание продукта, которое и так никто не читает',
                    price=uniform(0.01, 999_999.99), #случайная цена
                    quantity=randint(1, 10_000), #случайное количество
                    rating=uniform(0.01, 9.99), #случайный рейтинг
                    ))
            
        Product.objects.bulk_create(products) #принимает список объектов и продукты добавляются в бд все сразу за 1 раз