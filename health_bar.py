import os

os.system("")

class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    default_color = "\033[0m"

    def __init__(self,
                 entity,
                 length : int = 20,
                 is_colored : bool = True,
                 color : str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.max_health
        self.health = entity.health

        self.isColored = is_colored
        self.color = self.default_color
    
    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self) -> None:
        remaining_bard = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bard
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.max_health}")
        print(
            f"{self.barrier}"
            f"{remaining_bard * self.symbol_remaining}"
            f"{lost_bars * self.symbol_lost}"
            f"{self.default_color}"
            f"{self.barrier}"
        )