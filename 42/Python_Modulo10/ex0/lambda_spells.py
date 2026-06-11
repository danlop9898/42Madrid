from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(
    mages: list[dict[str, Any]],
    min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float | int]:

    powers = list(map(lambda m: m["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


def main() -> None:
    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
    ]
    artsort = artifact_sorter(artifacts)
    print(
        f"{artsort[0]['name']} ({artsort[0]['power']} power) comes before "
        f"{artsort[1]['name']} ({artsort[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transpell = spell_transformer(spells)
    print(transpell)

    print("\nTesting power filter...")
    mages = [
        {"name": "mage1", "power": 95, "element": "arcane"},
        {"name": "mage2", "power": 88, "element": "light"},
        {"name": "mage3", "power": 40, "element": "chaos"},
    ]

    filtered = power_filter(mages, 90)
    print(filtered)

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    main()
