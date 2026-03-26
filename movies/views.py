from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
from .services import *

@api_view(['POST'])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        clear_cache()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def bulk_create_movies(request):
    serializer = MovieSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        clear_cache()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=404)

    serializer = MovieSerializer(movie, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        clear_cache(pk)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_movies(request):
    return Response(get_all_movies())


@api_view(['GET'])
def get_movie(request, pk):
    data = get_movie_by_id(pk)
    if not data:
        return Response(status=404)
    return Response(data)