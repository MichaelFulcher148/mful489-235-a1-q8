
class Genre:
    def __init__(self, a_name: str):
        self.genre_name = a_name
        self.__data_set_of_movies = list()

    def __repr__(self) -> str:
        return f'<Genre {self.__genre_name}>'

    def __eq__(self, other: 'Genre') -> bool:
        if not isinstance(other, Genre):
            return False
        return self.__genre_name == other.__genre_name

    def __lt__(self, other: 'Genre') -> bool:
        if not isinstance(other, Genre):
            return False
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, name: str):
        if isinstance(name, str):
            if name == '':
                self.__genre_name = None
            else:
                self.__genre_name = name
        else:
            raise TypeError

    @property
    def data_set_of_movies(self) -> list:
        return self.__data_set_of_movies

    def add_movie(self, a_movie: 'Movie'):
        if isinstance(a_movie, Movie):
            self.__data_set_of_movies.append(a_movie)
        else:
            raise TypeError
