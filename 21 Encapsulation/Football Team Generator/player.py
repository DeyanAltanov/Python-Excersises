class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @property
    def endurance(self):
        return self.__endurance

    @property
    def sprint(self):
        return self.__sprint

    @property
    def dribble(self):
        return self.__dribble

    @property
    def passing(self):
        return self.__passing

    @property
    def shooting(self):
        return self.__shooting

    @name.setter
    def name(self, name):
        self.__name = name

    @endurance.setter
    def endurance(self, endurance):
        self.__endurance = endurance

    @sprint.setter
    def sprint(self, sprint):
        self.__sprint = sprint

    @dribble.setter
    def dribble(self, dribble):
        self.__dribble = dribble

    @passing.setter
    def passing(self, passing):
        self.__passing = passing

    @shooting.setter
    def shooting(self, shooting):
        self.__shooting = shooting

    def __str__(self):
        return f"Player: {self.__name}\nEndurance: {self.__endurance}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}\n"