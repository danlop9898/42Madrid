import sys


def main() -> None:

    cont = 1
    index = 0
    total = len(sys.argv)
    scores = [0] * (total - 1)

    while (cont < total):
        try:
            scores[index] = int(sys.argv[cont])
            index = index + 1
        except ValueError:
            print(f"Ignored invalid input: {sys.argv[cont]}")
        cont = cont + 1

    if index == 0:
        print("No valid scores provided!")
        return

    scores = scores[:index]

    print("=== Game Stats ===")
    print(f"Scores: {scores}")
    print(f"Count: {len(scores)}")
    print(f"Total: {sum(scores)}")
    print(f"Average: {sum(scores) / len(scores)}")
    print(f"Max: {max(scores)}")
    print(f"Min: {min(scores)}")
    print(f"Range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
