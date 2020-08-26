from datetime import datetime
from domainmodel.movie import Movie
from domainmodel.review import Review

def test_create_review():
    movie = Movie("Moana", 2016)
    review = Review(movie, "was pretty good", 9)
    the_time = datetime.today()
    assert str(review.movie) == f'<Movie Moana, 2016>'
    assert review.rating == 9
    assert review.review_text == 'was pretty good'
    assert str(review) == '<Review <Movie Moana, 2016>, was pretty good, 9, {}>'.format(the_time)

def test_compare_reviews():
    movie = Movie("Moana", 2016)
    review = Review(movie, "was pretty good", 9)
    review2 = Review(movie, "was pretty good", 9)
    assert review.timestamp == review2.timestamp
    assert review.movie == review2.movie
    assert review.review_text == review2.review_text
    assert review.rating == review2.rating
    assert (review == review2) is True

def test_review_ratings():
    movie = Movie("Moana", 2016)
    review = Review(movie, "was pretty good", -2)
    assert review.rating == None
    review = Review(movie, "was pretty good", 11)
    assert review.rating == None
    review = Review(movie, "was pretty good", 2)
    assert review.rating == 2
    review = Review(movie, "was pretty good", 0)
    assert review.rating == None

def test_review_timestamp():
    movie = Movie("Moana", 2016)
    review = Review(movie, "was pretty good", -2)
    the_time = datetime.today()
    assert str(the_time) == str(review.timestamp)
