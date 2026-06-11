from abc import ABC, abstractmethod
from ex0.creatures import Creature


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "transform")

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        result = []
        result.append(creature.transform())  # type: ignore
        result.append(creature.attack())
        result.append(creature.revert())  # type: ignore
        return "\n".join(result)


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )

        result = []
        result.append(creature.attack())
        result.append(creature.heal())  # type: ignore
        return "\n".join(result)
