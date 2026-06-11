import sys


def main()-> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    cont = 1
    total = len(sys.argv)

    if (total == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total - 1}")
        while (cont < total):
            print(f"Argument {cont}: {sys.argv[cont]}")
            cont = cont + 1
    print(f"Total arguments: {total}")


if __name__ == "__main__":
    main()
