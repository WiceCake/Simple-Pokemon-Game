import random
from health_bar import HealthBar

class Pokemon():

    def __init__(self, obj:dict) -> None:
        self.name = obj['name']
        self.type = obj['type']
        self.damage = obj['damage']
        self.health = obj['health']
        self.weakness = obj['weakness']
        self.attack_name = obj['attack_name']
        self.max_health = self.health
        self.displayDamage = self.damage

    def attack(self, target) -> None:
        self.displayDamage = random.randrange(self.damage - 5, self.damage)
        target.health -= self.displayDamage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.displayDamage} damage to "
              f"{target.name} with {self.attack_name}")

    def enhancement(self, target):
        if target.type in self.weakness:
            self.damage = round(self.damage / 2)

class Player(Pokemon):

    def __init__(self, obj:dict) -> None:
        super().__init__(obj=obj)
        self.health_bar = HealthBar(self, color="green")

class Enemy(Pokemon):

    def __init__(self, obj:dict) -> None:
        super().__init__(obj=obj)
        self.health_bar = HealthBar(self, color="red")


