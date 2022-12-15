from django.shortcuts import render, redirect
from .serializers import UserSerializer, HistorySerializer, MymenuSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import History, Mymenu


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

    # 히스토리 생성
    elif request.method == 'POST':
        # if Menu.objects.filter(request.data.menuname)
        history_serializer = HistorySerializer(data=request.data)
        if history_serializer.is_valid(raise_exception=True):
            history_serializer.save(user=request.user)

            menunames = request.data['menuname'].strip().split(' ')
            for i in range(len(menunames)):
                inst = {'name': menunames[i]}
                mymenu_serializer = MymenuSerializer(data=inst)
                if mymenu_serializer.is_valid():
                    history = History.objects.latest('id')
                    mymenu_serializer.save(history=history)

            return Response(history_serializer.data, status=status.HTTP_201_CREATED)


# 개별 히스토리 조회, 수정, 삭제
@api_view(['GET', 'DELETE', 'PUT'])
def history_detail(request, history_pk):

    history = History.objects.get(pk=history_pk) 
    user = request.user

    if request.method == 'GET':
        serializer = HistorySerializer(history)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if history.user_id == user.pk:
            history.delete()
            # Mymenu.objects.filter(history_id=history_pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'PUT':
        if history.user_id == user.pk:
            history_serializer = HistorySerializer(history, data=request.data)
            if history_serializer.is_valid(raise_exception=True):
                history_serializer.save()
                Mymenu.objects.filter(history_id=history_pk).delete()
                # menus = mymenus.values('name')
                # print(menus)

                menunames = request.data['menuname'].strip().split(' ')
                for i in range(len(menunames)):
                    inst = {'name': menunames[i]}
                    mymenu_serializer = MymenuSerializer(data=inst)
                    if mymenu_serializer.is_valid():
                        history = History.objects.latest('id')
                        mymenu_serializer.save(history=history)

                return Response(history_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

