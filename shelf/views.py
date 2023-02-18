from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Language, Author, Book

from rest_framework.viewsets import ModelViewSet
from .serializers import GenreSerializer, LanguageSerializer, AuthorSerializer, BookSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hola Mundo")

# Custom API
class GenreCustomAPI(APIView):
    def get(self, request):
        filtro_nombre = request.query_params.get('name')
        if filtro_nombre:
            genres = Genre.objects.filter(name__contains=filtro_nombre)
            serializer = GenreSerializer(genres, many=True)
        else:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
        
        return Response(serializer.data)


# ModelViewSet.
################################################################
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
