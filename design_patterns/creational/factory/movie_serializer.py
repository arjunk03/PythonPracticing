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
