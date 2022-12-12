from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from .models import History


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'nickname', 'message', 'image',)
        read_only_fields = ('username',)
        


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=50)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        return data



class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = '__all__'
        read_only_fields = ('user',)