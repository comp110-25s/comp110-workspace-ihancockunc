"""File to define River class."""

__author__: str = "730608493"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish and bears from the river simulation when too old."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes fish from the simulated river."""
        idx: int = 0
        while idx <= amount:
            self.fish.pop(idx)
            idx += 1
        return None

    def bears_eating(self):
        """Eats fish from the river and changes Bears' hunger scores."""
        while len(self.fish) >= 5:
            self.remove_fish(3)
            for bear in self.bears:
                bear.eat(3)
        return None

    def check_hunger(self):
        """Removes starving bears from the river simulation."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Adds baby fish to the existing fish in the river simulation."""
        baby_fish: int = (len(self.fish) // 2) * 4
        for _ in range(baby_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Adds baby bears to the bears in the river simulation."""
        baby_bears: int = len(self.bears) // 2
        for _ in range(baby_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Displays key river statistics during simulation."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        while self.day <= 7:
            self.one_river_day()
        return None
