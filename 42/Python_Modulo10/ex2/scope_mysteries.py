from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    cont: int = 0

    def counter() -> int:
        nonlocal cont
        cont += 1
        return cont

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:

    def accumulator(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:

    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("Testing mage counter...")

    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")

    ac1 = spell_accumulator(100)
    ac2 = spell_accumulator(100)

    print(f"ac1, add 20: {ac1(20)}")
    print(f"ac1, add 30: {ac1(30)}")
    print(f"ac2, add 50: {ac2(50)}")

    print("\nTesting enchantment factory...")

    flame = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")

    print(flame("Sword"))
    print(ice("Sword"))

    print("\nTesting memory vault...")

    vault = memory_vault()

    vault["store"]("secret", 123)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
