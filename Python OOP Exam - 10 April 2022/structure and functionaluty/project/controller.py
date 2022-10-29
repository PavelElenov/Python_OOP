class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_supply(self, sustenance_type):
        for i in range(len(self.supplies) - 1, -1, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                return self.supplies.pop(i)
        raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

    def __find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return

    def add_player(self, *args):
        successfully_added = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                successfully_added.append(player.name)
        return f"Successfully added: {', '.join(successfully_added)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name, sustenance_type):
        if sustenance_type in ['Food', 'Drink']:
            player = self.__find_player(player_name)
            if not player.need_sustenance:
                return f"{player_name} have enough stamina."
            supply = self.__find_supply(sustenance_type)

            if supply:
                player.stamina += supply.energy

                if player.stamina > 100:
                    player.stamina = 100
                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        def have_stamina(player):
            if player.stamina == 0:
                return False
            return True

        def check_for_winner(first_player, second_player):
            if first_player.stamina > second_player.stamina:
                if second_player.stamina < 0:
                    second_player.stamina = 0
                return f"Winner: {first_player.name}"
            else:
                if first_player.stamina < 0:
                    first_player.stamina = 0
                return f"Winner: {second_player.name}"

        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)

        if have_stamina(first_player):
            if have_stamina(second_player):
                if first_player.stamina > second_player.stamina:
                    first_player, second_player = second_player, first_player

                second_player.stamina -= first_player.stamina / 2
                first_player.stamina -= second_player.stamina / 2

                return check_for_winner(first_player, second_player)

            else:
                return f"Player {second_player.name} does not have enough stamina."
        else:
            if not have_stamina(second_player):
                return f"Player {first_player.name} does not have enough stamina.\n" \
                       f"Player {second_player.name} does not have enough stamina."
            return f"Player {first_player.name} does not have enough stamina."

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0

        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        ll = []

        for player in self.players:
            ll.append(player)

        for supply in self.supplies:
            ll.append(supply.details())

        return '\n'.join(str(x) for x in ll)
