from django.core.management.base import BaseCommand
from myapp2.models import User

# (venv) PS C:\Users\BOSS\Desktop\Django_code\myproject> python manage.py get_user 2
#передали 2 id или pk 

class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):#параметры передаем в командной строке
        parser.add_argument('pk', type=int, help='User ID')#'pk' -  имя аргумента командной строки

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']#из словаря kwargs по pk извлекаем значения которые передали в parser
        user = User.objects.filter(pk=pk).first() #найди пользователя в бд где айди совпадает first() - первый пользователь если пользователь не существует то none
        self.stdout.write(f'{user}')