from abc import ABC, abstractmethod
from ex0 import Creature
from ex1.new import TransformCapability, HealCapability
from typing import cast

class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid creature ´{creature.name}´ "
                "for this aggressive strategy"
            )
        transform_creature = cast(TransformCapability, creature)
        print(transform_creature.transform())
        result = transform_creature.attack()
        print(result)
        print(transform_creature.revert())
        return result


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid creature ´{creature.name}´ "
                "for this defensive strategy"
            )
        heal_creature = cast(HealCapability, creature)
        result = heal_creature.attack()
        print(result)
        print(heal_creature.heal())
        return result
