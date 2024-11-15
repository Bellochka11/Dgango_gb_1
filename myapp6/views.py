from django.shortcuts import render
from django.db.models import Sum
from myapp5.models import Product


def total_in_db(request): #запрос в бд общая сумма
    total = Product.objects.aggregate(Sum('quantity')) #aggregate - метод для агрегирования запросов в бд считаем сумму по всем столбцам
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_view(request): #сумма из представлений
    products = Product.objects.all() #извлекаю все продукты 
    total = sum(product.quantity for product in products) #суммирую все столбики quantity
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request): #сумма из шаблона 
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)