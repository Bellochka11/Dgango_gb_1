from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) #unique=True уникальное

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #on_delete=models.CASCADE если удалим категорию то удалятся все продукты из категории
    description = models.TextField(default='', blank=True) #описание blank=True не обязательное поле для заполнения
    price = models.DecimalField(default=999999.99, max_digits=8,decimal_places=2) # 8 - максимальное еол во чисел 2 после запятой 6 до суммарно 8
    quantity = models.PositiveSmallIntegerField(default=0) #количество
    date_added = models.DateTimeField(auto_now_add=True) #auto_now_add=True) поле автоматически заполняется
    rating = models.DecimalField(default=5.0, max_digits=3,decimal_places=2) #рейтинг максимум 3 цифры 2 после запятой

    def __str__(self):
        return self.name
    
    @property #свойство
    def total_quantity(self): #хочу взять все продукты и считаем сумму по quantity
        return sum(product.quantity for product in Product.objects.all())