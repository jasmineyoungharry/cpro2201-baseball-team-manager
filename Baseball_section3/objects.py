POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


class Player:
    def __init__(self, first_name: str, last_name: str, position: str, at_bats: int, hits: int):
        self.__first_name = first_name.strip()
        self.__last_name = last_name.strip()
        self.position = position
        self.update_stats(at_bats, hits)

    @property
    def full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}".strip()

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, value: str) -> None:
        value = value.strip().upper()
        if value not in POSITIONS:
            raise ValueError("Invalid position. Please try again.")
        self.__position = value

    @property
    def at_bats(self) -> int:
        return self.__at_bats

    @property
    def hits(self) -> int:
        return self.__hits

    def update_stats(self, at_bats: int, hits: int) -> None:
        at_bats = int(at_bats)
        hits = int(hits)
        if at_bats < 0 or hits < 0:
            raise ValueError("Invalid integer. Please try again.")
        if hits > at_bats:
            raise ValueError("Hits can't be greater than at bats.")
        self.__at_bats = at_bats
        self.__hits = hits

    @property
    def batting_average(self) -> float:
        if self.__at_bats == 0:
            return 0.0
        return self.__hits / self.__at_bats


class Lineup:
    def __init__(self, players=None):
        self.__players = list(players) if players else []

    def add_player(self, player: Player) -> None:
        self.__players.append(player)

    def remove_player(self, index: int) -> Player:
        return self.__players.pop(index)

    def move_player(self, old_index: int, new_index: int) -> None:
        player = self.__players.pop(old_index)
        self.__players.insert(new_index, player)

    def get_player(self, index: int) -> Player:
        return self.__players[index]

    def __len__(self) -> int:
        return len(self.__players)

    def __iter__(self):
        return iter(self.__players)

    def to_list(self):
        return list(self.__players)