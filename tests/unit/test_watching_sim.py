from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.user import User, Review, Movie
from domainmodel.genre import Genre
from domainmodel.watchlist import WatchList
from activitysimulations.watchingsimulation import MovieWatchingSimulation
from random import choice
import pytest

def create_movie_list(size_of_list: int, num_to_pick: int) -> list:
    options = [x for x in range(size_of_list)]
    if num_to_pick == 1:
        return [choice(options)]
    else:
        i = 0
        winners = list()
        while i < num_to_pick:
            winners.append(choice(options))
            options.remove(winners[-1])
            i += 1
        return winners

@pytest.fixture()
def the_sim():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    sim = MovieWatchingSimulation(movie_file_reader)
    sim.add_user(User("Paul", "wellington"))
    sim.add_user(User('jessica', 'piano'))
    return sim

def test_login_and_logout(the_sim):
    assert the_sim.user_login('paul', "wellington") is True
    assert the_sim.user_logout('paul') is True

def test_look_at_genre(the_sim):
    if the_sim.user_login("paul", "wellington"):
        # print("User Paul logged in")
        # print('look at genre, Adventure.')
        viewed_list = the_sim.look_at_genre("paul", 'Adventure')
        for i in viewed_list:
            assert isinstance(i, Movie) is True

def test_create_and_view_watchlist(the_sim):
    if the_sim.user_login("paul", "wellington"):
        # print("User Paul logged in")
        # print('look at genre, Adventure.')
        viewed_list = the_sim.look_at_genre("paul", 'Adventure')
        # print("pick some movies")
        user_picks = create_movie_list(len(viewed_list), 15)
        # print(user_picks)
        # print(viewed_list[user_picks[1]])
        for i in user_picks:
            the_sim.add_to_watchlist("paul", viewed_list[i])
        # print("paul views his watchlist")
        new_watchlist = the_sim.get_watchlist("paul")
        assert new_watchlist[1] == viewed_list[user_picks[1]]
        the_sim.user_logout("Paul")
        # print("Paul logged out")

def test_simulate_CS235_watching_session(the_sim):
    if the_sim.user_login("paul", "wellington"):
        viewed_list = the_sim.look_at_genre("paul", 'Adventure')
        user_picks = create_movie_list(len(viewed_list), 15)
        for i in user_picks:
            the_sim.add_to_watchlist("paul", viewed_list[i])
        new_watchlist = the_sim.get_watchlist("paul")
        the_message = the_sim.play_movie("paul", new_watchlist[1])
        movie_title = new_watchlist[1].title
        assert 'here is {} stream'.format(movie_title) == the_message
        the_sim.play_movie('paul', new_watchlist[4])
        total_play_in_minutes = new_watchlist[1].runtime_minutes + new_watchlist[4].runtime_minutes
        assert total_play_in_minutes == the_sim.time_watched_in_minues('paul')
        the_sim.user_logout("Paul")

def test_share_a_movie(the_sim):
    if the_sim.user_login("paul", "wellington"):
        viewed_list = the_sim.look_at_genre("paul", 'Adventure')
        user_picks = create_movie_list(len(viewed_list), 15)
        a_movie = viewed_list[user_picks[3]]
        the_sim.share_movie('paul', a_movie, 'jessica')
        the_sim.user_login('jessica', 'piano')
        new_watchlist = the_sim.get_received_movies("jessica")
        assert (a_movie in new_watchlist) == True
        the_sim.user_logout("Paul")
        the_sim.user_logout("jessica")