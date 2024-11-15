from django.core.management.base import BaseCommand
from myapp2.models import User

# (venv) PS C:\Users\BOSS\Desktop\Django_code\myproject> python manage.py get_user_age_greater 40

class Command(BaseCommand):
    help = "Get user with age greater <age>."

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age') 
    def handle(self, *args, **kwargs):
        age = kwargs['age']
        user = User.objects.filter(age__gt=age) #age__gt - в столбике возраст найти всех у кого age больше чем то число которое передали gt-значение поля больше заданного значения
        self.stdout.write(f'{user}')

