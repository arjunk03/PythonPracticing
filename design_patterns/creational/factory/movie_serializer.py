import json
import xml.etree.ElementTree as et


class MovieSerializer:
    __fmt_dictionary = {}

    def __init__(self, fmt, serializer_fn):
        self.__fmt_dictionary[fmt] = serializer_fn

    @classmethod
    def serialize(cls, movie, fmt):
        if fmt not in cls.__fmt_dictionary:
            raise ValueError("Invalid format")

        return cls.__fmt_dictionary[fmt](movie)


class JsonMovieSerializer(MovieSerializer):
    def __init__(self):
        MovieSerializer.__init__(self, "JSON", self.__serialize_to_json)

    def __serialize_to_json(self, movie):
        return json.dumps(
            {"id": movie.movie_id, "name": movie.movie_name,
                "director": movie.director}
        )


class XmlMovieSerializer(MovieSerializer):
    def __init__(self):
        MovieSerializer.__init__(self, "XML", self.__serialize_to_xml)

    def __serialize_to_xml(self, movie):
        movie_info = et.Element("movie", attrib={"id": movie.movie_id})
        name = et.SubElement(movie_info, "name")
        name.text = movie.movie_name
        director = et.SubElement(movie_info, "director")
        director.text = movie.director
        return et.tostring(movie_info, encoding="unicode")


JsonMovieSerializer()
XmlMovieSerializer()
