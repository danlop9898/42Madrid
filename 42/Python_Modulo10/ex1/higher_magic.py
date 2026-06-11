from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:

    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplifier


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def main() -> None:
    print("Testing spell combiner...")

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print("Combined result:", result)

    print("\nTesting power amplifier...")

    mega_fireball = power_amplifier(fireball, 3)
    original = fireball("Dragon", 10)
    amplified = mega_fireball("Dragon", 10)

    print("Original:", original)
    print("Amplified:", amplified)

    print("\nTesting conditional caster...")

    def enough_power(target: str, power: int) -> bool:
        return power >= 20

    safe_fireball = conditional_caster(enough_power, fireball)

    print(safe_fireball("Dragon", 30))
    print(safe_fireball("Dragon", 10))

    print("\nTesting spell sequence...")

    spells: list[Callable[[str, int], str]] = [fireball, heal]

    combo = spell_sequence(spells)
    sequence_result: list[str] = combo("Dragon", 10)
    print("Sequence result:", sequence_result)

    print("Sequence result:", result)


if __name__ == "__main__":
    main()
