from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(operator.add, spells)

    if operation == "multiply":
        return reduce(operator.mul, spells)

    if operation == "max":
        return max(spells)

    if operation == "min":
        return min(spells)

    return 0


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:

    fire: Callable[[str], str] = partial(base_enchantment, 50, "fire")
    ice: Callable[[str], str] = partial(base_enchantment, 50, "ice")
    light: Callable[[str], str] = partial(base_enchantment, 50, "light")

    return {
        "fire": fire,
        "ice": ice,
        "light": light
    }


def memoized_fibonacci(n: int) -> int:

    @lru_cache(maxsize=None)
    def fib(x: int) -> int:
        if x < 2:
            return x
        return fib(x - 1) + fib(x - 2)

    return fib(n)


def spell_dispatcher() -> Callable[..., str]:

    @singledispatch
    def dispatch(value: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(value: int) -> str:
        return f"{value} damage"

    @dispatch.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatch.register
    def _(value: list) -> str:  # type: ignore
        return f"Multi-cast: {len(value)} spells"

    return dispatch


def main() -> None:

    print("Testing spell reducer...")

    spells = [10, 20, 30, 40]

    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting memoized fibonacci...")

    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.73457))

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} {target} with power {power}"

    enchants = partial_enchanter(base_enchantment)

    print(enchants["fire"]("sword"))
    print(enchants["ice"]("sword"))
    print(enchants["light"]("sword"))


if __name__ == "__main__":
    main()
