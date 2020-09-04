from domainmodel.movie import Movie
from domainmodel.genre import Genre
from domainmodel.user import User
from domainmodel.review import Review
from domainmodel.watchlist import WatchList
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from random import randint

class MovieWatchingSimulation:
    def __init__(self, movie_reader: 'MovieFileCSVReader') -> None:
        self.__movie_list = movie_reader
        self.__user_data = dict()
        self.__who_is_logged_in = list()

    '''Watchlist @ 1 is the users watchlist, Watchlist @ 2 is movies shared to the user'''
    def add_user(self, a_user: 'User'):
        if isinstance(a_user, User):
            self.__user_data[a_user.username] = [a_user, WatchList(), WatchList()]
        else:
            raise TypeError

    def user_login(self, name: str, password: str) -> bool:
        name.strip().lower()
        if name in self.__user_data:
            if password == self.__user_data[name][0].password:
                self.__who_is_logged_in.append(name)
                return True
        return False

    def user_logout(self, name: str) -> bool:
        try:
            self.__who_is_logged_in.remove(name.strip().lower())
            return True
        except ValueError:
            pass

    def check_user_is_logged_in(self, a_name):
        if a_name in self.__who_is_logged_in:
            return True
        return False

    def look_at_genre(self, name: str, a_genre: str):
        if not self.check_user_is_logged_in(name):
            return
        genre = Genre(a_genre.strip())
        if genre in self.__movie_list.dataset_of_genres:
            return self.__movie_list.get_movies_of_genre(genre)

    def add_to_watchlist(self, name: str, a_movie: 'Movie'):
        if not self.check_user_is_logged_in(name):
            return
        if a_movie in self.__movie_list.dataset_of_movies:
            self.__user_data[name][1].add_movie(a_movie)

    def get_watchlist(self, name: str):
        if not self.check_user_is_logged_in(name):
            return
        a_list = list()
        for i in self.__user_data[name][1]:
            a_list.append(i)
        return a_list

    def find_movie_in_database(self, a_movie: 'Movie') -> 'Movie':
        i = 0
        active_database = self.__movie_list.dataset_of_movies
        length = len(active_database)
        while i < length:
            if active_database[i] == a_movie:
                return i
            i += 1
        return -1

    def play_movie(self, name: str, a_movie: 'Movie'):
        if not self.check_user_is_logged_in(name):
            return 'Not logged in'
        o = self.find_movie_in_database(a_movie)
        if o != -1:
            self.__user_data[name][0].watch_movie(a_movie)
            return 'here is {} stream'.format(self.__movie_list.dataset_of_movies[o].title)
        else:
            return "Movie not found"

    def time_watched_in_minues(self, name: str) -> int:
        if not self.check_user_is_logged_in(name):
            return 0
        return self.__user_data[name][0].time_spent_watching_movies_minutes

    def share_movie(self, name: str, a_movie: 'Movie', destination: str):
        if not self.check_user_is_logged_in(name):
            return 0
        if destination in self.__user_data.keys():
            self.__user_data[destination][2].add_movie(a_movie)

    def get_received_movies(self, name: str) -> list:
        if not self.check_user_is_logged_in(name):
            return 0
        a_list = list()
        for i in self.__user_data[name][2]:
            a_list.append(i)
        return a_list

    def go(self) -> None:
        pass
        # user_1 = User("Paul", "wellington")
        # user_1_watchlist = WatchList()
        # for i in self.create_movie_list(12):
        #     user_1_watchlist.add_movie(self.__movie_list.dataset_of_movies[i])
        # print("what is {}'s first movie? - {}".format(user_1.username, user_1_watchlist.first_movie_in_watchlist()))
        # print("{} watches {}".format(user_1.username, user_1_watchlist.first_movie_in_watchlist()))
        # user_1.watch_movie(user_1_watchlist.first_movie_in_watchlist())
        # print("{} has spent {} minutes and watched:".format(user_1.username, user_1.time_spent_watching_movies_minutes))
        # print(user_1.watched_movies)
        # print('\n')
        # user_2 = User("Mark", "taupo343")
        # user_2_watchlist = WatchList()
        # for i in self.create_movie_list(15):
        #     user_2_watchlist.add_movie(self.__movie_list.dataset_of_movies[i])
        # print("what is {}'s third movie? - {}".format(user_2.username, user_2_watchlist.select_movie_to_watch(2)))
        # print("{} watches {}".format(user_2.username, user_2_watchlist.select_movie_to_watch(2)))
        # user_2.watch_movie(user_2_watchlist.select_movie_to_watch(2))
        # print("what is {}'s first movie? - {}".format(user_2.username, user_2_watchlist.first_movie_in_watchlist()))
        # print("{} watches {}".format(user_2.username, user_2_watchlist.first_movie_in_watchlist()))
        # user_2.watch_movie(user_2_watchlist.first_movie_in_watchlist())
        # print("{} has spent {} minutes and watched:".format(user_2.username, user_2.time_spent_watching_movies_minutes))
        # print(user_2.watched_movies)
        # print('\n')
        # user_3 = User("Sarah", "thaskullz")
        # user_3_watchlist = WatchList()
        # for i in self.create_movie_list(7):
        #     user_3_watchlist.add_movie(self.__movie_list.dataset_of_movies[i])
        # for i in range(3):
        #     user_3.watch_movie(user_3_watchlist.select_movie_to_watch(i))
        # print("{} has spent {} minutes and watched:".format(user_3.username, user_3.time_spent_watching_movies_minutes))
        # print(user_3.watched_movies)
        # print('\n')
        # user_1.add_review(Review(user_1_watchlist.select_movie_to_watch(4), "Very nice", 7))
        # print('user {} added {}'.format(user_1.username, user_1.reviews[0]))
        # print('\n')
        # user_2.add_review(Review(user_2_watchlist.first_movie_in_watchlist(), "Awesome", 10))
        # user_2.add_review(Review(user_2_watchlist.select_movie_to_watch(2), "Aweful", 2))
        # print('user {} added Reviews:'.format(user_2.username))
        # for i in user_2.reviews:
        #     print(i)
