import random


def gen_player_archievements(archs: list[str]) -> set[str]:

    random1 = random.randint(1, 9)
    player = set(random.sample(archs, random1))
    return player


def main() -> None:
    print("=== Archievement Tracker System ===")
    archs = [
        "arch1", "arch2", "arch3", "arch4",
        "arch5", "arch6", "arch7", "arch8",
        "arch9", "arch10"
    ]
    player1 = gen_player_archievements(archs)
    player2 = gen_player_archievements(archs)
    player3 = gen_player_archievements(archs)
    player4 = gen_player_archievements(archs)
    print(f"Player Alice: {player1}")
    print(f"Player Bob: {player2}")
    print(f"Player Charlie: {player3}")
    print(f"Player Dylan: {player4}")
    print()

    all_archs = player1 | player2 | player3 | player4
    common = player1 & player2 & player3 & player4
    player1_only = player1 - player2 - player3 - player4
    player2_only = player2 - player1 - player3 - player4
    player3_only = player3 - player1 - player2 - player4
    player4_only = player4 - player1 - player2 - player3
    archs_parser = set(archs)
    player1_missing = archs_parser - player1
    player2_missing = archs_parser - player2
    player3_missing = archs_parser - player3
    player4_missing = archs_parser - player4
    print(f"All distinct achievements: {all_archs}")
    print()
    print(f"Common achievements: {common}")
    print()

    print(f"Only Alice has: {player1_only}")
    print(f"Only Bob has: {player2_only}")
    print(f"Only Charlie has: {player3_only}")
    print(f"Only Dylan has: {player4_only}")
    print()
    print(f"Alice is missing: {player1_missing}")
    print(f"Bob is missing: {player2_missing}")
    print(f"Charlie is missing: {player3_missing}")
    print(f"Dylan is missing: {player4_missing}")


if __name__ == "__main__":
    main()
