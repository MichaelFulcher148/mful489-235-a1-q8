
class Genre:
    def __init__(self, a_name: str):
        self.genre_name = a_name

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
