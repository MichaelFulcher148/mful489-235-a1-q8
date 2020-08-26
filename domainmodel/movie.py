from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, name: str, year: int):
        self.title = name
        self.release_year = year
        self.__actors_list = list()
        self.__genres_list = list()
        self.__description = None
        self.__director = None
        self.__runtime_minutes = None

    def __repr__(self) -> str:
        return f'<Movie {self.__title}, {self.__release_year}>'

    def __eq__(self, other: 'Movie') -> bool:
        if isinstance(other, Movie):
            return self.__title == other.title and self.__release_year == other.release_year
        return False

    def __lt__(self, other: 'Movie') -> bool:
        if isinstance(other, Movie):
            if self.__title < other.title:
                return True
            elif self.__title == other.title:
                return self.__release_year < other.release_year
        return False

    def __hash__(self) -> int:
        return hash((self.__title, self.__release_year))

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, year: int):
        if isinstance(year, int):
            if year >= 1900:
                self.__release_year = year
            else:
                raise ValueError
        else:
            raise TypeError

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, name: str):
        if isinstance(name, str):
            self.__title = name
        else:
            raise TypeError

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, text: str):
        if isinstance(text, str):
            self.__description = text
        else:
            raise TypeError

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, a_director: 'Director'):
        if isinstance(a_director, Director):
            self.__director = a_director
        else:
            raise TypeError

    @property
    def actors(self) -> list:
        return self.__actors_list

    @actors.setter
    def actors(self, list_of_actors: list):
        if isinstance(list_of_actors, list):
            self.__actors_list = list_of_actors
        else:
            raise TypeError

    @property
    def genres(self) -> list:
        return self.__genres_list

    @genres.setter
    def genres(self, list_of_genres: list):
        if isinstance(list_of_genres, list):
            self.__genres_list = list_of_genres
        else:
            raise TypeError

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, minutes: int):
        if isinstance(minutes, int) and minutes > 0:
            self.__runtime_minutes = minutes
        else:
            raise ValueError

    def add_actor(self, a_actor: 'Actor'):
        if isinstance(a_actor, Actor):
            if a_actor not in self.__actors_list:
                self.__actors_list.append(a_actor)
        else:
            raise TypeError

    def remove_actor(self, b_actor: 'Actor'):
        if isinstance(b_actor, Actor):
            try:
                self.__actors_list.pop(self.__actors_list.index(b_actor))
            except ValueError:
                pass
        else:
            raise TypeError

    def add_genre(self, a_genre: 'Genre'):
        if isinstance(a_genre, Genre):
            if a_genre not in self.__genres_list:
                self.__genres_list.append(a_genre)
        else:
            raise TypeError

    def remove_genre(self, b_genre: 'Genre'):
        if isinstance(b_genre, Genre):
            try:
                self.__genres_list.pop(self.__genres_list.index(b_genre))
            except ValueError:
                pass
        else:
            raise TypeError
