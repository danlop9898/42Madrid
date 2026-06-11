def input_temperature(temp_str: str) -> int:

    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


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
    try:
        data3 = "100"
        print(f"Input data is '{data3}'")
        temp = input_temperature(data3)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    try:
        data4 = "-50"
        print(f"Input data is '{data4}'")
        temp = input_temperature(data4)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print()
    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
