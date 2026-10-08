from ex1 import HealingCreatureFactory, TransformCreatureFactory
from typing import cast

def main() -> None:

    print("Testing Creature with healing capability base:")
    healing_factory = HealingCreatureFactory()
    creature_1 = healing_factory.create_base()
    print(creature_1.describe())
    print(creature_1.attack())
    print(creature_1.heal())
    print("evolved:")
    creature_2 = healing_factory.create_evolved()
    print(creature_2.describe())
    print(creature_2.attack())
    print(creature_2.heal())
    print("\nTesting Creature with transform capability base:")
    transform_factory = TransformCreatureFactory()
    creature_1 = transform_factory.create_base()
    print(creature_1.describe())
    print(creature_1.attack())
    print(creature_1.transform())
    print(creature_1.attack())
    print(creature_1.revert())
    print("evolved:")
    creature_2 = transform_factory.create_evolved()
    print(creature_2.describe())
    print(creature_2.attack())
    print(creature_2.transform())
    print(creature_2.attack())
    print(creature_2.revert())


if __name__ == "__main__":
    main()
