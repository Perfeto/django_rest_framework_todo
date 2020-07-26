from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from testapp.models import ToDoTask
from testapp.serializers import ToDoTaskSerializer


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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ToDoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer
    permission_classes = [IsAuthenticated]


########################################################################################################################

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
