#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> float:
        growth = round(0.8, 1)
        self.height = round(self.height + growth, 1)
        return growth

    def age_one_day(self) -> None:
        self.age = self.age + 1


def main() -> None:
    plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    plant.show()

    day = 1
    initial_height = plant.height
    while (day <= 7):
        plant.grow()
        plant.age_one_day()
        plant.show()
        day = day + 1
    print(f"Growth this week: {round(plant.height - initial_height, 1)}cm")


if __name__ == "__main__":
    main()
