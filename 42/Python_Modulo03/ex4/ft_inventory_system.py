import sys


def main() -> None:
    inventory: dict[str, int] = {}

    cont = 1

    print("=== Inventory System Analysis ===")
    while cont < len(sys.argv):
        arg = sys.argv[cont]

        temp = ""
        item = ""
        qty_str = ""

        points = 0

        i = 0
        while i < len(arg):
            if arg[i] == ":":
                points += 1
            i += 1

        if points != 1:
            print(f"Error- invalid parameter '{arg}'")
            cont += 1
            continue

        i = 0
        while i < len(arg):
            if arg[i] == ":":
                item = temp
                temp = ""
            else:
                temp += arg[i]
            i += 1

        qty_str = temp

        if item == "" or qty_str == "":
            print(f"Error- invalid parameter '{arg}'")
            cont += 1
            continue

        try:
            qty = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            cont += 1
            continue

        if item in inventory:
            print(f"Redundant item '{item}'- discarding")
        else:
            inventory[item] = qty

        cont += 1

    if len(inventory) == 0:
        print("Inventory is empty")
        return

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    totalsum = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {totalsum}")

    for item in inventory:
        perc = (inventory[item] / totalsum) * 100
        print(f"Item {item} represents {round(perc,1)}%")

    items = list(inventory.keys())

    most = items[0]

    for item in items:
        if inventory[item] > inventory[most]:
            most = item

    print(f"Item most abundant: {most} with quantity {inventory[most]}")

    least = items[0]

    for item in items:
        if inventory[item] < inventory[least]:
            least = item

    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory["magic_item"] = 1

    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
