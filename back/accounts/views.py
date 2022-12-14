from django.shortcuts import render, redirect
from .serializers import UserSerializer, HistorySerializer, MymenuSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import History


# 유저 프로필 조회 및 수정
@api_view(['GET', 'PUT'])
def profile(request, username):
    
    User = get_user_model()

    if request.method == 'GET':
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)   
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user.username == username:
            serializer = UserSerializer(request.user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(username = request.user.username)
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# 전체 히스토리 조회
@api_view(['GET', 'POST'])
def history(request):

    if request.method == 'GET':
        histories = History.objects.filter(user=request.user.id)
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # if Menu.objects.filter(request.data.menuname)
        history_serialzier = HistorySerializer(data=request.data)
        if history_serialzier.is_valid(raise_exception=True):
            history_serialzier.save(user=request.user)

            menunames = request.data['menuname'].strip().split(' ')
            for i in range(len(menunames)):
                inst = {'name': menunames[i]}
                mymenu_serializer = MymenuSerializer(data=inst)
                if mymenu_serializer.is_valid():
                    history = History.objects.latest('id')
                    mymenu_serializer.save(history=history)

            return Response(history_serialzier.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def history_detail(request, history_pk):

    if request.method == 'GET':
        history = History.objects.get(pk=history_pk)
        serialzier = HistorySerializer(history)
        return Response(serialzier.data)


