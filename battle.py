from ex0 import AquaFactory, FlameFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    creature = factory.create_evolved()
    print(creature.describe())
    print(creature.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:

    print("Testing factory")
    test_factory(FlameFactory())
    print("\nTesting factory")
    test_factory(AquaFactory())

    print("\nTesting battle!")
    battle(FlameFactory(), AquaFactory())

if __name__ == "__main__":
    main()
