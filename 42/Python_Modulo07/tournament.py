from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy

Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***\n")
    print(f"{len(opponents)} opponents involved\n")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):

                factory1, strategy1 = opponents[i]
                factory2, strategy2 = opponents[j]

                c1 = factory1.create_base()
                c2 = factory2.create_base()

                print("* Battle *\n")
                print(c1.describe())
                print("vs.\n")
                print(c2.describe())
                print("now fight!\n")

                if not strategy1.is_valid(c1):
                    raise Exception(
                        f"Invalid Creature '{c1.name}' for this strategy"
                    )

                if not strategy2.is_valid(c2):
                    raise Exception(
                        f"Invalid Creature '{c2.name}' for this strategy"
                    )

                print(strategy1.act(c1))
                print(strategy2.act(c2))
                print()

    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")
        return


def format_opponents(opponents: List[Opponent]) -> List[Tuple[str, str]]:
    return [
        (factory.__class__.__name__.replace("Factory", ""),
         strategy.__class__.__name__.replace("Strategy", ""))
        for factory, strategy in opponents
    ]


if __name__ == "__main__":

    print("Tournament 0 (basic)\n")

    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]

    print(format_opponents(opponents))
    battle(opponents)

    print("\nTournament 1 (error)\n")

    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]

    print(format_opponents(opponents))
    battle(opponents)

    print("\nTournament 2 (multiple)\n")

    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]

    print(format_opponents(opponents))
    battle(opponents)
