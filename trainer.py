from pokemon import Pokemon
from random import choice

class Trainer:
    def __init__(self, name, team, inventory):
        self.name = name
        self.team = team
        self.inventory = inventory

    def catch_pokemon(self, wild_pokemon):
        if wild_pokemon.is_wild and len(self.team) < 6:
            self.team.append(wild_pokemon)
            wild_pokemon.is_wild = False
            print(f"{self.name} caught {wild_pokemon.name}!")
        else:
            print("Can't catch this Pokémon!")

    def use_item(self, item, target):
        item.use(target)

    def battle(self, opponent):
        print(f"{self.name} is battling {opponent.name}!")
        my_pokemon = self.team[0]
        opponent_pokemon = opponent.team[0]

        while my_pokemon.current_health > 0 and opponent_pokemon.current_health > 0:
            print(f"\n{my_pokemon.name} (HP: {my_pokemon.current_health}) vs {opponent_pokemon.name} (HP: {opponent_pokemon.current_health})")

            move = self.choose_move(my_pokemon)
            my_pokemon.attack_opponent(move, opponent_pokemon)

            if opponent_pokemon.current_health > 0:
                move = choice(opponent_pokemon.moves)
                opponent_pokemon.attack_opponent(move, my_pokemon)

        if my_pokemon.current_health > 0:
            print(f"{my_pokemon.name} won the battle!")
            self.gain_experience(100)
        else:
            print(f"{my_pokemon.name} fainted!")

    def choose_move(self, pokemon):
        print(f"Choose a move for {pokemon.name}:")
        for idx, move in enumerate(pokemon.moves):
            print(f"{idx + 1}. {move.name} ({move.type} type, {move.power} power, {move.accuracy * 100}% accuracy)")
        choice = int(input("Enter the number of the move you want to use: ")) - 1
        return pokemon.moves[choice]

    def gain_experience(self, exp):
        for pokemon in self.team:
            pokemon.gain_experience(exp)
