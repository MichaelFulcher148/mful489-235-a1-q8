from domainmodel.watchlist import WatchList
from domainmodel.movie import Movie

def test_create_watch_list():
    watchlist = WatchList()
    assert (f"Size of watchlist: {watchlist.size()}") == f"Size of watchlist: 0"
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert str(watchlist.first_movie_in_watchlist()) == '<Movie Moana, 2016>'

def test_check_size():
    watchlist = WatchList()
    assert (f"Size of watchlist: {watchlist.size()}") == f"Size of watchlist: 0"
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert (f"Size of watchlist: {watchlist.size()}") == f"Size of watchlist: 3"

def test_remove_movie():
    watchlist = WatchList()
    assert (f"Size of watchlist: {watchlist.size()}") == f"Size of watchlist: 0"
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    assert str(watchlist.first_movie_in_watchlist()) == '<Movie Moana, 2016>'
    watchlist.remove_movie(Movie("Moana", 2016))
    assert (f"Size of watchlist: {watchlist.size()}") == f"Size of watchlist: 1"
    assert str(watchlist.first_movie_in_watchlist()) == '<Movie Ice Age, 2002>'

def test_select_movie():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert watchlist.select_movie_to_watch(1) == Movie("Ice Age", 2002)
    assert watchlist.select_movie_to_watch(2) == Movie("Guardians of the Galaxy", 2012)
    assert watchlist.select_movie_to_watch(3) == None

def test_check_first_movie():
    watchlist = WatchList()
    assert watchlist.first_movie_in_watchlist() == None
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    assert watchlist.first_movie_in_watchlist() == Movie("Moana", 2016)

def test_iterator():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    a_list = [Movie("Moana", 2016), Movie("Ice Age", 2002), Movie("Guardians of the Galaxy", 2012)]
    n = 0
    for i in watchlist:
        assert i == a_list[n]
        n += 1
    iter_obj = iter(watchlist)
    n = 0
    while n != len(a_list):
        assert iter_obj.__next__() == a_list[n]
        n += 1