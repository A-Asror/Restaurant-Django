from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm, ContactForm

@login_required(login_url='login_page')# Перенаправляет пользователя в другую страницу если он не прошел аунтетификацию (sign in)
def index(request):
    """
     Функция для вывода главную страницу сайта
    """
    return render(request, 'mainapp/index.html')


def register_page(request):
    """
    Фунция для Регистрации пользователя (sign up)
    """
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            if request.method == 'POST':
                messages.error(request, 'Ваш Пароль не достаточно сложный')
    context = {
        'form': form,
    }
    return render(request, 'mainapp/login.html', context)


def login_page(request):
    """
    Функция для аунтетификации пользователя (sign in)
    """
    if request.user.is_authenticated:
        redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(123465)
            user = authenticate(request, username=username, email=email, password=password)

            if user is not None:
                login(request, user)
                print(777777777777777)
                return redirect('home')
            else:
                messages.info(request, 'ERROR')
        context = {}

        return render(request, 'mainapp/login.html', context)


def logout_user(request):
    """
    Функция для выхода из аккаунта в сайте (logout)
    """
    logout(request)
    return redirect('login_page')


@login_required(login_url='login_page')
def contact(request):
    """
    Функця для закакза столика с ресторана
    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'mainapp/contact.html', context)


@login_required(login_url='login_page')
def menu(request):
    """
     ГЛАВНАЯ Функция который выводит основной функционал сайта
     выводит категориев, поваров, еду и может сортировать
    """
    categories = Category.objects.all()
    products = Product.objects.all()
    chefs = Chefs.objects.all()
    print('ВСЕ ПРОДУКТЫ ПРОЧИТАНЫ')
    if request.method == 'POST' and request.POST.get('category_id'):
        products = Product.objects.filter(category=request.POST.get('category_id'))
        print('ЗАПРОС ЕСТЬ И products ОТФИЛЬТЕРОВАЛСЯ')
    elif request.method == 'POST' and request.POST.get():
        products = Product.objects.all()
        print('ПОЛЬЗОВАТЕЛЬ НЕ ВЫБРАЛ Кутегорию НО ЗАПРОС ЕСТЬ')
    else:
        products = Product.objects.all()
        print('В ДРУГИХ СЛУЧАЯХ ТОЖЕ ПРОДУКТЫ СУЩЕСТВУЮТ')
    context = {
        'products': products,
        'category': categories,
        'chefs': chefs
    }
    return render(request, 'mainapp/menu.html', context)


def name_categories():
    """
    Эта функция просто для себя, фукция берет все категории,
    блюды и повара, смотрю везде вызываю одно и тоже и решил
    вывести в другую функцию
    """
    categories = Category.objects.all()
    products = Product.objects.all()
    chefs = Chefs.objects.all()
    context = {
        'chefs': chefs,
        'product': products,
        'category': categories
    }
    return context
