from django.contrib import admin
from .models import Category, Product

@admin.action(description="Сбросить количество в ноль") # изменение queryset данные из бд подсказка
def reset_quantity(modeladmin, request, queryset): #сбросить количество
    queryset.update(quantity=0) #обновляем то что выделили галочкой и устанавливаем 0

class ProductAdmin(admin.ModelAdmin): #будет добавлено в админку но не в бд
    # """Список продуктов."""
    list_display = ['name', 'category', 'quantity']
    ordering=['category','-quantity'] #- сортировка по убыванию
    list_filter = ['date_added', 'price'] #сортировка данных фильтрация справа
    search_fields = ['description'] #поле для поиска поиск по описанию
    search_help_text = 'Поиск по полю Описание продукта (description)' #подсказка поле для поиска
    actions = [reset_quantity] #действие
    # """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'date_added','rating'] #поля которые хочу видеть
    readonly_fields = ['date_added', 'rating'] #поля для чтения дата добавления обязательно
    fieldsets = [ # не дружит с fields закоментировали множество полей задаем значения
        (
            None, #поле без названия
            {
                'classes': ['wide'], #большое поле
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'], #схлопнулось
                'description': 'Категория товара и его подробное описание', #описание
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
