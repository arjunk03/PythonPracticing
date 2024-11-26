import json
import xml.etree.ElementTree as et


class Movie:
    def __init__(self, movie_id, movie_name, director):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.director = director


# class MovieSerializer:
#     def serialize(self, movie, fmt):
#         if fmt == "JSON":
#             movie_info = {
#                 "id": movie.movie_id,
#                 "name": movie.movie_name,
#                 "director": movie.director,
#             }
#             return json.dumps(movie_info)
#         elif fmt == "XML":
#             movie_info = et.Element("movie", attrib={"id": movie.movie_id})
#             name = et.SubElement(movie_info, "name")
#             name.text = movie.movie_name
#             director = et.SubElement(movie_info, "director")
#             director.text = movie.director
#             return et.tostring(movie_info, encoding="unicode")
#         else:
#             raise ValueError("Invalid format")
#


class MovieSerializer:
    def serialize(self, movie, fmt):
        if fmt == "JSON":
            return self.__serialize_to_json(movie)
        elif fmt == "XML":
            return self.__serialize_to_xml(movie)
        else:
            raise ValueError("Invalid format")

    def __serialize_to_json(self, movie):
        return json.dumps(
            {"id": movie.movie_id, "name": movie.movie_name, "director": movie.director}
        )

    def __serialize_to_xml(self, movie):
        movie_info = et.Element("movie", attrib={"id": movie.movie_id})
        name = et.SubElement(movie_info, "name")
        name.text = movie.movie_name
        director = et.SubElement(movie_info, "director")
        director.text = movie.director
        return et.tostring(movie_info, encoding="unicode")


movie = Movie("1", "The Matrix", "Lana Wachowski")
serializer = MovieSerializer()
serialized_movie = serializer.serialize(movie, "JSON")
print(serialized_movie)
serialized_movie = serializer.serialize(movie, "XML")
print(serialized_movie)
