from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.user import User, Review, Movie
from domainmodel.genre import Genre
from domainmodel.watchlist import WatchList
from activitysimulations.watchingsimulation import MovieWatchingSimulation
from random import choice

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

def main():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    the_sim = MovieWatchingSimulation(movie_file_reader)
    ##the_sim.go()
    the_sim.add_user(User("Paul", "wellington"))
    if the_sim.user_login("paul", "wellington"):
        print("User Paul logged in")
        print('look at genre, Adventure.')
        viewed_list = the_sim.look_at_genre("paul", 'Adventure')
        print("pick some movies")
        user_picks = create_movie_list(len(viewed_list), 15)
        print(user_picks)
        print(viewed_list[user_picks[1]])
        for i in user_picks:
            the_sim.add_to_watchlist("paul", viewed_list[i])
        print("paul views his watchlist")
        new_watchlist = the_sim.get_watchlist("paul")
        assert new_watchlist[1]== viewed_list[user_picks[1]]
    if the_sim.user_logout("Paul"):
        print("Paul logged out")

if __name__ == "__main__":
    main()