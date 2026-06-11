from typing import cast
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex0.factory import CreatureFactory


def test_healing_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")

    base = factory.create_base()
    evolved = factory.create_evolved()

    base_heal = cast(HealCapability, base)
    evolved_heal = cast(HealCapability, evolved)

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base_heal.heal())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved_heal.heal())


def test_transform_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")

    base = factory.create_base()
    evolved = factory.create_evolved()

    base_tr = cast(TransformCapability, base)
    evolved_tr = cast(TransformCapability, evolved)

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base_tr.transform())
    print(base.attack())
    print(base_tr.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved_tr.transform())
    print(evolved.attack())
    print(evolved_tr.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_factory(healing_factory)
    print()
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()
