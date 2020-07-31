from django.urls import path

from testapp import views

urlpatterns = [
    path('todotasks/', views.ToDoItemsList.as_view()),
    path('todotask/<int:pk>/', views.ToDoItemDetail.as_view()),

    path('user/', views.UserCreate.as_view())
]
