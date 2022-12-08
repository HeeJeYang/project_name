from rest_framework import serializers
from .models import User
from .models import History


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'nickname', 'message', 'image',)


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = '__all__'