from django.core.management.base import BaseCommand
from myapp2.models import User
# (venv) PS C:\Users\BOSS\Desktop\Django_code\myproject> python manage.py get_all_users

class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        users = User.objects.all() #нужны все объекты строки из бд
        self.stdout.write(f'{users}') #вывод