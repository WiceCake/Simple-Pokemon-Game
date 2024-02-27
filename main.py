from pokemon import Player, Enemy
from data import pokemons
import random

player = int(input("<--Choose your pokemon-->"
                   "\n1. Bulbasur"
                   "\n2. Squirtle"
                   "\n3. Charmander"
                   "\nEnter the selected number: "))

player = Player(pokemons[player-1])
enemy = Enemy(pokemons[random.randrange(0,2)-1])


player.enhancement(enemy)
enemy.enhancement(player)

while True:

    player.attack(enemy)
    enemy.attack(player)

    player.health_bar.draw()
    enemy.health_bar.draw()

    if player.health <= 0:
        print(f"Your pokemon {player.name} lost!!!")
        break
    elif enemy.health <= 0 :
        print(f"Your pokemon {player.name} win!!!")
        break
    elif enemy.health == 0 and player.health:
        print(f"The fight concludes draw!!")
        break

    input()