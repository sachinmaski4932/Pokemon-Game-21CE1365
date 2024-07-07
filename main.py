from move import Move
from pokemon import Pokemon
from trainer import Trainer
from item import Item

# Defining moves
thunderbolt = Move("Thunderbolt", "Electric", 90, 1.0, "special")
tackle = Move("Tackle", "Normal", 40, 1.0, "physical")

# Defining characters
pikachu = Pokemon("Pikachu", "Electric", 100, 55, 40, 50, 50, 90, 5, 0, [thunderbolt, tackle], False)
bulbasaur = Pokemon("Bulbasaur", "Grass", 100, 49, 49, 65, 65, 45, 5, 0, [tackle], True)
ash = Trainer("Ash", [pikachu], [])

# Catching random pokemon //if any 
ash.catch_pokemon(bulbasaur)
# Fighting
misty = Trainer("Misty", [bulbasaur], [])
ash.battle(misty)
