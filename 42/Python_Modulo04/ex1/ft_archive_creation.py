import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Error arguments")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        f = open(sys.argv[1], "r")

        content = f.read()
        print("--")
        print(content, end="")
        print("--")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")

        lines: list[str] = []
        current_line = ""

        for ch in content:
            if ch != "\n":
                current_line += ch
            else:
                lines = lines + [current_line]
                current_line = ""

        if current_line != "":
            lines = lines + [current_line]

        transformed: list[str] = []

        for line in lines:
            transformed = transformed + [line + "#"]

        new_content = ""

        for line in transformed:
            new_content += line + "\n"

        print("Transform data:")
        print("--")
        print(new_content, end="")
        print("--")

        filename = input("Enter new file name (or empty): ")

        if filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{filename}'")

            f2 = open(filename, "w")
            f2.write(new_content)
            f2.close()

            print(f"Data saved in file '{filename}'.")

    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")

    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
