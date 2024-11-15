from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse #ответ
from django.views.generic import TemplateView #представления на основе классов
from django.shortcuts import render, get_object_or_404 #возвращает объект из бд если не получилось то 404
from .models import Author, Post

def hello(request): # request запрос
    return HttpResponse("Hello World from function!")

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")
    
def year_post(request, year):
    text = ""
    # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")

class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")
    
def post_detail(request, year, month, slug):
# Формируем статьи за год и месяц по идентификатору.
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False}) #в моем json объекте будут не только символы кодировки англ но и русских буктв т.к. в титле и контент русские буквы 

def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context) #запрос, шаблон контекст

class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html" #имя шаблона

    def get_context_data(self, **kwargs): #распаковка словаря
        context = super().get_context_data(**kwargs) #обращаемся к родителькому шаблону плюс свои
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context
    
def view_for(request):
    my_list=['apple','banana','orange']
    my_dict={
        'каждый':'красный',
        'охотник':'оранжевый',
        'желает':'жёлтый',
        'знать':'зелёный',
        'где':'голубой',
        'сидит':'синий',
        'фазан':'фиолетовый',
    }
    context={'my_list':my_list,'my_dict':my_dict}
    return render(request,'myapp3/templ_for.html',context)

def index(request):
    return render(request, 'myapp3/index.html')

def about(request):
    return render(request, 'myapp3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id) #извлекли автора
    posts = Post.objects.filter(author=author).order_by('-id')[:5] #Отфильтруй посты по ключу автор  order_b сортировка по id в обратном порядке от большого к меньшему 5 записей с большими id
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})

def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id) #найди посты
    return render(request, 'myapp3/post_full.html', {'post': post})