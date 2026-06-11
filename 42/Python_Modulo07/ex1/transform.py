from ex0.creatures import Creature
from .capabilities import TransformCapability


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.is_transformed:
            return "Shiftling attacks normally."
        return "Shiftling performs a boosted strike!"

    def transform(self, target: str | None = None) -> str:
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self, target: str | None = None) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.is_transformed:
            return "Morphagon attacks normally."
        return "Morphagon unleashes a devastating morph strike!"

    def transform(self, target: str | None = None) -> str:
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self, target: str | None = None) -> str:
        self.is_transformed = False
        return "Morphagon stabilizes its form."
