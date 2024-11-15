from django.db import models

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
