from django.core.cache import cache
from .models import Movie

CACHE_TIMEOUT = 300

def get_all_movies():
    key = "movies_all"
    data = cache.get(key)

    if not data:
        data = list(Movie.objects.all().values())
        cache.set(key, data, CACHE_TIMEOUT)

    return data


def get_movie_by_id(movie_id):
    key = f"movie_{movie_id}"
    data = cache.get(key)

    if not data:
        try:
            data = Movie.objects.values().get(id=movie_id)
            cache.set(key, data, CACHE_TIMEOUT)
        except Movie.DoesNotExist:
            return None

    return data


def clear_cache(movie_id=None):
    cache.delete("movies_all")
    if movie_id:
        cache.delete(f"movie_{movie_id}")