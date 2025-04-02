import movie_serializer


class Movie:
    def __init__(self, movie_id, movie_name, director):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.director = director


movie = Movie("1", "The Matrix", "Lana Wachowski")
movie_info = movie_serializer.MovieSerializer.serialize(movie, "JSON")
print(movie_info)
movie_info = movie_serializer.MovieSerializer.serialize(movie, "XML")
print(movie_info)
