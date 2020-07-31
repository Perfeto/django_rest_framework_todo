from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from testapp.models import ToDoTask
from testapp.serializers import ToDoTaskSerializer, UserRegistrationSerializer
from testapp.services.ToDoTaskService import get_todo_tasks_for_user, on_task_created_telegram_notify


class ToDoItemsList(generics.ListCreateAPIView):
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_tasks = get_todo_tasks_for_user(self.request.user.pk)
        return Response(user_tasks)

    def perform_create(self, serializer: ToDoTaskSerializer):
        serializer.save(owner=self.request.user)
        on_task_created_telegram_notify(serializer.data.get('id'))


class ToDoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer
    permission_classes = [IsAuthenticated]


########################################################################################################################

class UserCreate(generics.CreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserRegistrationSerializer
