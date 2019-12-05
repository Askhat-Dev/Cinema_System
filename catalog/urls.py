from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rating/', views.rating, name="rating"),
    path('contacts/', views.contacts, name="contacts"),
    path('cabinet/', views.cabinet, name="cabinet"),
    path('film1/', views.film1, name="film1"),
    path('register/', views.RegisterFormView.as_view(), name='register'),

]