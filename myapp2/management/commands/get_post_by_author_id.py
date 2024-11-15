from django.core.management.base import BaseCommand
from myapp2.models import Author, Post

class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    # def handle(self, *args, **kwargs): # ТУТ ИЗВЛЕКАЕМ ИМЯ АВТОРА ЧЕРЕЗ ОБЪЕКТ АВТОРА
    #     pk = kwargs.get('pk')
    #     author = Author.objects.filter(pk=pk).first() #находим первого автора с совпадающим айди
    #     if author is not None:
    #         posts = Post.objects.filter(author=author) #находим ВСЕ посты
    #         intro = f'All posts of {author.name}\n'
    #         text = '\n'.join(post.content for post in posts) #перебираем все посты извлекаем content
    #         self.stdout.write(f'{intro}{text}')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)#нужен столбец автора. в столбце автора из таблицы Post проверяем первичный ключ
        intro = f'All posts\n'
        # text = '\n'.join(post.content for post in posts) #тут извлеакем весь контент
        text = '\n'.join(post.get_summary() for post in posts) #тут обращаемся к функции в модели и извлеакем первые 12 слов
        self.stdout.write(f'{intro}{text}')