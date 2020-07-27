from django.contrib.auth.models import User
from rest_framework import serializers

from testapp.models import ToDoTask


class ToDoTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ToDoTask
        fields = ['id', 'title', 'description', 'owner', 'change_date', 'status']


class UserSerializer(serializers.ModelSerializer):
    to_do_items = serializers.PrimaryKeyRelatedField(many=True, queryset=ToDoTask.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'to_do_items']
