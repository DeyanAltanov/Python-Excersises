from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def validate_player_name(self, player: Player):
        for p in self.players:
            if p.name == player.name:
                raise Exception(f"Name {player.name} is already used!")

    def add_player(self, *players):
        result = f"Successfully added: "
        initial_result = result
        for player in players:
            if player not in self.players:
                self.validate_player_name(player)
                self.players.append(player)
                result += f"{player.name}, "
        if initial_result == result:
            return result
        return result[:-2]

    def add_supply(self, *supplies):
        for supply in supplies:
            if supply not in self.supplies:
                self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type):
        if self.check_player_availability(player_name):
            if self.check_supply_availability(sustenance_type):
                sustenance = self.check_supply_availability(sustenance_type)
                self.increase_stamina(player_name, sustenance)
                return f"{player_name} sustained successfully with {sustenance.name}."
        if sustenance_type == 'Food':
            raise Exception("There are no food supplies left!")
        else:
            raise Exception("There are no drink supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        player_1: Player = None
        player_2: Player = None
        for player in self.players:
            if player.name == first_player_name:
                player_1 = player
            if player.name == second_player_name:
                player_2 = player
        if player_1.stamina == 0:
            return f"Player {player_1.name} does not have enough stamina."
        if player_2.stamina == 0:
            return f"Player {player_2.name} does not have enough stamina."
        if player_1.stamina == 0 and player_2.stamina == 0:
            return f"Player {player_1.name} does not have enough stamina.\n"f"Player {player_2.name} does not have enough stamina."
        if player_1.stamina < player_2.stamina:
            first_player = player_1
            second_player = player_2
        else:
            first_player = player_2
            second_player = player_1
        while True:
            second_player.stamina -= first_player.stamina * 0.5
            if second_player.stamina <= 0:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"
            first_player.stamina -= second_player.stamina * 0.5
            if first_player.stamina <= 0:
                first_player.stamina = 0
                return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            value = player.age * 2
            if player.stamina - value <= 0:
                player.stamina = 0
            else:
                player.stamina -= value
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def check_supply_availability(self, sustenance_type):
        for supply in range(len(self.supplies) - 1, 0, -1):
            if self.supplies[supply].__class__.__name__ == sustenance_type:
                return self.supplies[supply]

    def check_player_availability(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return True

    def remove_supply(self, sustenance_type):
        for supply in range(len(self.supplies) - 1, 0, -1):
            if self.supplies[supply].name == sustenance_type.name:
                self.supplies.remove(self.supplies[supply])
                break

    def increase_stamina(self, player_name, sustenance_type):
        for player in self.players:
            if player.name == player_name:
                if player.stamina == 100:
                    return f"{player_name} have enough stamina."
                elif player.stamina + sustenance_type.energy > 100:
                    player.stamina = 100
                    self.remove_supply(sustenance_type)
                    break
                else:
                    player.stamina += sustenance_type.energy
                    self.remove_supply(sustenance_type)
                    break