from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import *



class MainView(TemplateView):
    template_name = 'main.html'


class ShopView(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        games = Game.objects.all()
        print(games)
        context['games'] = games
        return context


class CartView(TemplateView):
    template_name = 'cart.html'


def sign_up_by_django(request):
    error = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if User.objects.filter(login=login).exists():
                error = "Такой пользователь уже существует!"
            elif password != repeat_password:
                error = "Пароли не совпадают!"
            else:
                User.objects.create(login=login,
                                    password=password,
                                    age=age)
    else:
        form = UserRegisterForm()

    context = {
        'info': error,
        'form': form
    }
    print(context)

    return render(request,
                  'registration.html',
                  context=context)
