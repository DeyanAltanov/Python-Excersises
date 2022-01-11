class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player not in self.players and player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        filtered = [player for player in self.players if player.name == player_name]
        if filtered:
            self.players.remove(filtered[0])
            filtered[0].guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += f"Name: {player.name}\nGuild: {player.guild}\nHP: {player.hp}\nMP: {player.mp}\n"
            for skill, mana_cost in player.skills.items():
                result += f"==={skill} - {mana_cost}\n"
        return result