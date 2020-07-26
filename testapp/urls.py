from django.urls import path

from testapp import views

urlpatterns = [
    path('hello/with/token/', views.HelloView.as_view(), name='helloWithToken'),

    path('todotasks/', views.ToDoItemsList.as_view()),
    path('todotask/<int:pk>/', views.ToDoItemDetail.as_view()),
]
