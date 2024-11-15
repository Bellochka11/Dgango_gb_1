from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget
import logging
from django.shortcuts import render
from .models import User
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm


logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == 'POST': #проверка пост или гет запроса
        form = UserForm(request.POST)
        if form.is_valid(): #если данные прошли валидацию
            name = form.cleaned_data['name'] #проверенные данные
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp4/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})



def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES) # POST текст FILES набор байт файл от пользователя на сервер
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage() #файлы 
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form': form})