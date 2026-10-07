from abc import ABC, abstractmethod
from ex0 import CreatureFactory, Creature

class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):

    def __init__(self) -> None:
        self.is_transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass
    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"


class Bloomelle(Creature, HealCapability):

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "Grass")


    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class Shiftling(Creature, TransformCapability):

    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.is_transformed = False

    def transform(self) -> str:
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."
    
    def attack(self) -> str:
        if not self.is_transformed:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"


class Morphagon(Creature, TransformCapability):

    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.is_transformed = False

    def transform(self) -> str:
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Morphagon stabilizes its form."
    
    def attack(self) -> str:
        if not self.is_transformed:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"
    
class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")


    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")
