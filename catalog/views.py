from django.shortcuts import render
from django.views import generic
from .models import Movie, Producer, MovieInstance, Genre


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Movie.objects.all()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books}
    )


def rating(request):
    return render(
        request, 'rating.html',
        context={})

def contacts(request):
    return render(
        request, 'contacts.html',
        context={})
def cabinet(request):
    return render(
        request, 'cabinet.html',
        context={})
def film1(request):
    return render(
        request, 'film1.html',
        context={})

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
