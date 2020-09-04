import pytest
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User
 
def test_create_user():
    user = User('Mike', 'nope')
    assert str(user) == '<User mike>'

def test_compare_user():
    user = User('mike', 'nope')
    user2 = User('paul', 'nope')
    user3 = User('mike', 'nuddo')
    assert (user == user2) == False
    assert (user == user3) == True

def test_add_review_to_user():
    user = User('mike', 'nope')
    movie = Movie("Moana", 2016)
    review = Review(movie, "was pretty good", 9)
    user.add_review(review)
    assert user.reviews == [review]

def test_add_watched_movies():
    user = User('mike', 'nope')
    movie = Movie("Moana", 2016)
    movie.runtime_minutes = 88
    movie2 = Movie("Total Recall", 1989)
    movie2.runtime_minutes = 90
    total_time = movie2.runtime_minutes + movie.runtime_minutes
    user.watch_movie(movie)
    user.watch_movie(movie2)
    assert user.time_spent_watching_movies_minutes == total_time
    assert user.watched_movies == [movie, movie2]

def test_user_less_than():
    user = User('mike', 'nope')
    user2 = User('paul', 'nope')
    assert (user < user2) == True