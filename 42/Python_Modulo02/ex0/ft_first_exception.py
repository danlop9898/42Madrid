def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        data1 = "25"
        print(f"Input data is '{data1}'")
        temp = input_temperature(data1)
        print(f"Temperature is now {temp}ºC")
        print()
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    try:
        data2 = "abc"
        print(f"Input data is '{data2}'")
        temp = input_temperature(data2)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Temperature Input Test ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
