from django.urls import path

from telegrambot import views

urlpatterns = [
    path('addtelegram/', views.TelegramProfileCreate.as_view()),
]
