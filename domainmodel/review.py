from datetime import datetime

from domainmodel.movie import Movie

class Review:
    def __init__(self, movie: 'Movie', review: str, rating: int) -> None:
        self.__movie_ref = movie
        self.__review_text = review
        if 0 < rating < 11:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.today()

    def __repr__(self):
        return f'<Review {self.__movie_ref}, {self.__review_text}, {self.__rating}, {self.__timestamp}>'

    def __eq__(self, other):
        return self.__movie_ref == other.movie and self.__review_text == other.review_text \
               and self.__rating == other.rating and self.__timestamp == other.timestamp

    @property
    def movie(self):
        return self.__movie_ref

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp
