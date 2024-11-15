from django.core.management.base import BaseCommand
from myapp2.models import User
# (venv) PS C:\Users\BOSS\Desktop\Django_code\myproject> python manage.py create_user  

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        #user = User(name='John', email='john@example.com', password='secret', age=25)
        #user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        user = User(name='Jack', email='neo@example.com', password='secret', age=58)
        user.save() #сохраняю
        self.stdout.write(f'{user}') #в консоль