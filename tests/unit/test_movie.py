import pytest
from domainmodel.user import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

def test_create_Director():
    burg = Director('Stephen burg')
    assert burg.__repr__() == f'<Director Stephen burg>'

def test_compare_Director():
    burg = Director('Stephen burg')
    director = Director('Stephen burg')
    director2 = Director('Tom')
    assert (burg == director) == True
    assert (director2 == director) == False

def test_create_Actor():
    cofner = Actor('Cevin Cofner')
    assert cofner.__repr__() == f'<Actor Cevin Cofner>'

def test_create_Genre():
    action = Genre('Action')
    assert action.__repr__() == f'<Genre Action>'

def test_create_Movie():
    movie = Movie("Moana", 2016)
    assert movie.title == 'Moana'
    assert movie.release_year == 2016
    assert movie.__repr__() == f'<Movie Moana, 2016>'
    ##assert movie.__hash__() == -5820196721283855152

def test_compare_Movie():
    movie = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    movie3 = Movie("Lethal Weapon", 1985)
    movie4 = Movie("Lethal Bandanna", 1985)
    movie5 = Movie("Moanb", 2016)
    assert (movie == movie2) == True
    assert (movie == movie3) == False
    assert (movie3 == movie4) == False
    assert (movie5 == movie2) == False

def test_compare_lt_Movie():
    movie = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    movie3 = Movie("Lethal Weapon", 1985)
    movie4 = Movie("Lethal Bandanna", 1985)
    movie5 = Movie("Moanb", 2016)
    movie6 = Movie("Moanb", 2018)
    assert (movie < movie2) == False
    assert (movie < movie3) == False
    assert (movie3 < movie) == True
    assert (movie3 < movie4) == False
    assert (movie5 < movie2) == False
    assert (movie2 < movie5) == True
    assert (movie5 < movie6) == True

def test_add_director():
    direc = Director("John Candy")
    movie = Movie("Moana", 2016)
    movie.director = direc
    assert movie.director.__repr__() == f'<Director John Candy>'

def test_change_release_year():
    movie = Movie("Moana", 2016)
    movie.release_year = 1902
    assert movie.release_year == 1902
    with pytest.raises(ValueError):
        movie.release_year = 1830
    with pytest.raises(TypeError):
        movie.release_year = '1830'

def test_change_title():
    movie = Movie("Moana", 2016)
    movie.title = 'The Blob'
    assert movie.title == 'The Blob'
    with pytest.raises(TypeError):
        movie.title = 1830

def test_add_actor():
    actor1 = Actor("Angelina Jolie")
    movie = Movie("Moana", 2016)
    movie.add_actor(actor1)
    assert movie.actors == [Actor("Angelina Jolie")]

def test_add_actors():
    movie = Movie("Moana", 2016)
    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    movie.actors = actors
    assert movie.actors == [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]

def test_remove_actor():
    movie = Movie("Moana", 2016)
    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    movie.actors = actors
    movie.remove_actor(Actor("Dwayne Johnson"))
    assert movie.actors == [Actor("Auli'i Cravalho"), Actor("Rachel House"), Actor("Temuera Morrison")]

def test_add_genre():
    movie = Movie("Moana", 2016)
    cartoon = Genre('Cartoon')
    movie.genres = [cartoon]
    assert movie.genres == [Genre('Cartoon')]

def test_remove_genre():
    movie = Movie("Moana", 2016)
    movie.genres = [Genre('Cartoon'), Genre('Kids'), Genre('Action')]
    movie.remove_genre(Genre('Action'))
    assert movie.genres == [Genre('Cartoon'), Genre('Kids')]

def test_add_movie_run_time():
    movie = Movie("Moana", 2016)
    movie.runtime_minutes = 107
    assert movie.runtime_minutes == 107
