from ex0.factory import CreatureFactory
from ex0.creatures import Creature


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        from .healing import Sproutling
        return Sproutling()

    def create_evolved(self) -> Creature:
        from .healing import Bloomelle
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        from .transform import Shiftling
        return Shiftling()

    def create_evolved(self) -> Creature:
        from .transform import Morphagon
        return Morphagon()
