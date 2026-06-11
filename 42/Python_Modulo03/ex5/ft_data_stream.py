import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]

    while (True):
        player1 = random.choice(players)
        action1 = random.choice(actions)
        tuple1 = (player1, action1)
        yield tuple1


def consume_event(
    lista: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(lista) > 0:
        index = random.randint(0, len(lista) - 1)
        item = lista[index]

        lista = lista[:index] + lista[index+1:]

        print(f"Got event from list: {item}")
        print(f"Remains in list: {lista}")

        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list10: list[tuple[str, str]] = []

    for i in range(10):
        list10 = list10 + [next(gen)]

    print(f"Built list of 10 events: {list10}")

    for event in consume_event(list10):
        pass


if __name__ == "__main__":
    main()
