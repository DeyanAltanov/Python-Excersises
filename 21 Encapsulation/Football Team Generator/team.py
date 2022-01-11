class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def players(self):
        return self.__players

    @name.setter
    def name(self, name):
        self.__name = name

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for player in self.__players:
            if player_name == player.name:
                self.__players.remove(player)
            return player
        return f"Player {player_name} not found"