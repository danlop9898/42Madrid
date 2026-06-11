#!/usr/bin/env python3
from typing import Type


class Plant:

    class _Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0

        def inc_grow(self) -> None:
            self._grow += 1

        def inc_age(self) -> None:
            self._age += 1

        def inc_show(self) -> None:
            self._show += 1

        def inc_shade(self) -> None:
            self._shade += 1

        def display(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(
                f"Stats: {self._grow} grow, {self._age}"
                f"age, {self._show} show"
            )

    def __init__(
        self,
        name: str = "Unknown plant",
        height: float = 0.0,
        age: int = 0
    ) -> None:
        self.name = name
        self.height = height
        self.age = age
        self._stats = Plant._Stats()

    @staticmethod
    def older_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls: Type["Plant"]) -> "Plant":
        return cls()

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age

    def set_height(self, height: float) -> None:
        if height > 0:
            self.height = height

    def set_age(self, age: int) -> None:
        if age > 0:
            self.age = age

    def show(self) -> None:
        self._stats.inc_show()
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self, amount: float) -> None:
        self.height += amount

        if self.name == "Rose":
            self.height += 0.8
        elif self.name == "Sunflower":
            self.height += 1
        elif self.name == "Cactus":
            self.height += 1.3

        self._stats.inc_grow()

    def age_up(self) -> None:
        self.age += 1
        self._stats.inc_age()

    def show_stats(self) -> None:
        self._stats.display(self.name)


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.num_seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.num_seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.num_seeds}")


class Tree(Plant):

    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def inc_shade(self) -> None:
            self._shade += 1

        def display(self, name: str) -> None:
            super().display(name)
            print(f"{self._shade} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree._TreeStats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter}cm wide."
        )
        self._stats.inc_shade()

    def show_stats(self) -> None:
        self._stats.display(self.name)


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self.nutritional_value += 2

    def age_up(self) -> None:
        super().age_up()
        self.nutritional_value += 1


def show_plant_stats(plant: Plant) -> None:
    plant.show_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_year(400)}")

    print("=== Flower")

    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.show_stats()

    print("[asking the rose to grow and bloom]")

    rose.grow(8)
    rose.bloom()

    rose.show()
    rose.show_stats()

    print("=== Tree")

    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.show_stats()

    oak.produce_shade()
    oak.show_stats()

    print("[asking the oak to produce shade]")

    oak.produce_shade()
    oak.show_stats()

    print("=== Seed")

    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    sunflower.show_stats()

    print("[make sunflower grow, age and bloom]")

    sunflower.grow(30)
    sunflower.age_up()
    sunflower.bloom()

    sunflower.show()
    sunflower.show_stats()

    print("=== Anonymous")

    unknown = Plant.anonymous()
    unknown.show()
    unknown.show_stats()

    show_plant_stats(unknown)


if __name__ == "__main__":
    main()
