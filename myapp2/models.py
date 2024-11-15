from django.db import models


class User(models.Model): #модель 4 столбца в таблице юзер id добавит джанго сам
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self): #информация выводится в консоль об юзере
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2) #max_digits=8 максимум чисел decimal_places=2 рубли и копейки
    description = models.TextField()
    image = models.ImageField(upload_to='products/') #изображения в каталоге products/

class Order(models.Model): #заказчик
    customer = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=models.CASCADE- при уадлении пользователя удалются все его заказы
    products = models.ManyToManyField(Product) #1 продукт может быть в нескольких заказах и заказы могут содержать один и тот же продукт
    date_ordered = models.DateTimeField(auto_now_add=True) #auto_now_add=True автоматическая дата добавляется
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #on_delete=models.CASCADE при удалении автора удаляем все его посты автор может написать несколько постов
    
    def __str__(self):
        return f'Title is {self.title}'
    
    def get_summary(self):
        words = self.content.split() #взяли контент и разделили по словам
        return f'{" ".join(words[:8])}...' #извлекли 8 слов
