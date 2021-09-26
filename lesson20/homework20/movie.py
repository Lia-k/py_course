from __future__ import annotations

from typing import List
from xml.etree import ElementTree


class Movie:
    def __init__(
        self,
        title: str,
        format_movie: str,
        year: int,
        rating: str,
    ):
        self.title = title
        self.format_movie = format_movie
        self.year = year
        self.rating = rating

    @classmethod
    def from_xml(cls, path: str) -> List[Movie]:
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        movies_class = []

        for movie in collection.iter('movie'):
            movies.append(movie)
        for element in movies:
            movies_class.append(cls(*element))
        return movies_class


if __name__ == '__main__':
    movies = Movie.from_xml("market.xml")
