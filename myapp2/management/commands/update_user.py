from django.core.management.base import BaseCommand
from myapp2.models import User

# (venv) PS C:\Users\BOSS\Desktop\Django_code\myproject> python manage.py update_user 2 Max   

class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID') #ключ
        parser.add_argument('name', type=str, help='User name') #имя пользователя

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name #присваиваем имя которое передали в командной строке
        user.save()
        self.stdout.write(f'{user}')