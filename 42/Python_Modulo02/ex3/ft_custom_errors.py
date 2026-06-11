class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def plant_check(plant: int) -> None:
    if (plant > 100):
        raise PlantError("The tomato plant is wilting!")


def water_check(plant: int) -> None:
    if (plant < 100):
        raise WaterError("Not enough water in the tank!")


def main():
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        plant_check(150)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        water_check(50)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    try:
        plant_check(150)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        water_check(50)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
