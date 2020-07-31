from django.contrib.auth.models import User
from rest_framework import serializers

from testapp.models import ToDoTask


class ToDoTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ToDoTask
        fields = ['id', 'title', 'description', 'owner', 'change_date', 'status']


class UserSerializer(serializers.ModelSerializer):
    to_do_list = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ToDoTask.objects.all(),
        required=False
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'to_do_list', ]


class UserRegistrationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
