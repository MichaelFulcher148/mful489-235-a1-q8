
class Actor:
    def __init__(self, name: str):
        self.actor_full_name = name
        self.colleague_list = list()

    def __repr__(self) -> str:
        return f'<Actor {self.__actor_full_name}>'

    def __eq__(self, other: 'Actor') -> bool:
        if not isinstance(other, Actor):
            return False
        return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other: 'Actor') -> bool:
        if not isinstance(other, Actor):
            return False
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self) -> int:
        return hash(self.__actor_full_name)

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self, name: str):
        if isinstance(name, str):
            if name == '':
                self.__actor_full_name = None
            else:
                self.__actor_full_name = name
        else:
            raise TypeError

    def add_actor_colleague(self, colleague: 'Actor'):
        self.colleague_list.append(colleague)

    def check_if_this_actor_worked_with(self, colleague: 'Actor') -> bool:
        for a in self.colleague_list:
            if colleague == a:
                return True
        return False

