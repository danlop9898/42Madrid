#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    plant1 = Plant("Rose", 15, 10)

    print(
        f"Plant created: {plant1.name}: "
        f"{plant1.get_height()}cm, {plant1.get_age()} days old"
    )

    plant1.set_height(25)
    plant1.set_age(30)

    plant1.set_height(-10)
    plant1.set_age(-10)

    print("Current state:", end=" ")
    plant1.show()


if __name__ == "__main__":
    main()
