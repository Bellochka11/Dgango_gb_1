from django.core.management.base import BaseCommand


# (venv) PS C:\Users\BOSS\Desktop\Django_code\myproject> python manage.py my_command 

#команды
class Command(BaseCommand):
    help = "Print 'Hello world!' to output." #справка
    def handle(self, *args, **kwargs): #ключевые и позиционные аргументы
        self.stdout.write('Hello world!') #вывод инфы в консоль