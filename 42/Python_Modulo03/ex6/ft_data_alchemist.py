import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
    ]
    players_capitalize = [name.capitalize() for name in players]
    players_capitalize_only = [name for name in players if name.istitle()]
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {players_capitalize}")
    print(f"New list of capitalized name only: {players_capitalize_only}")

    scores = {name: random.randint(0, 1000) for name in players_capitalize}
    avg = sum(scores.values())/len(scores)
    high_scores = {
        name: score for name,
        score in scores.items() if score > avg
    }
    print(f"Score dict: {scores}")
    print(f"Score averange is: {round(avg, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
