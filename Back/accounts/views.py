from django.shortcuts import render, redirect
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# 유저 프로필 조회 및 수정
@api_view(['GET', 'PUT'])
def profile(request):

    if request.method == 'GET':
        serializer = UserSerializer(request.user)   
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(username = request.user.username)
            return Response(serializer.data)
