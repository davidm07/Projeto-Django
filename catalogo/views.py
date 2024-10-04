from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Filme
from . import serializers


# Create your views here.
@api_view(['GET', 'POST'])
def getFilmes(request):
    if request.method == 'GET':
        filmes = Filme.objects.all()
        serializer = serializers.FilmeSerializer(filmes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = serializers.FilmeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)