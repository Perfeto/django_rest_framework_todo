from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from telegrambot.Bot import TelegramBot
from telegrambot.models import TelegramProfile
from testapp.models import ToDoTask
from testapp.serializers import ToDoTaskSerializer, UserRegistrationSerializer


class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World! Nice to meat you, ' + str(request.user)}
        return Response(content)


class ToDoItemsList(generics.ListCreateAPIView):
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        to_do_items_list = ToDoTask.objects.filter(owner=request.user)
        serializer = ToDoTaskSerializer(instance=to_do_items_list, many=True)
        return_data = serializer.data
        return Response(return_data)

    def perform_create(self, serializer: ToDoTaskSerializer):
        serializer.save(owner=self.request.user)
        saved_to_do_task = \
            ToDoTask.objects.filter(id=serializer.data.get('id')).first()

        telegram_user = \
            TelegramProfile.objects.filter(user_id=self.request.user.pk).first()

        TelegramBot().send_text_to_telegram(saved_to_do_task.__str__(), telegram_user.external_id)


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
