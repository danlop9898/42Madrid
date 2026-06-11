def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        2/0
    elif operation_number == 2:
        open("aaaaaaaa.txt", "r")
    elif operation_number == 3:
        "a" + 2  # type: ignore


def test_temperature() -> None:
    print("=== Garden Error Types Demo ===")
    cont = 0
    while (cont <= 4):
        print(f"Testing operation {cont}...")
        try:
            garden_operations(cont)
            if cont == 4:
                print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        cont = cont + 1
    print()
    print("All error types tested successfully!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
