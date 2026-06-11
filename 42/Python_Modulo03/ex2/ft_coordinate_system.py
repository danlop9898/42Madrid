import math


def get_player_pos() -> tuple[float, float, float]:

    while True:
        dates = input("Enter new coordinates as float in format 'x,y,z': ")
        temp = ""
        cont = 0
        contstring = 0
        x = ""
        y = ""
        z = ""

        try:
            while (cont < len(dates)):

                if (dates[cont] != ","):
                    temp = temp + dates[cont]
                else:
                    if (contstring == 0):
                        x = temp
                    elif (contstring == 1):
                        y = temp

                    temp = ""
                    contstring = contstring + 1
                cont = cont + 1
            z = temp
            if contstring != 2:
                print("Invalid syntax")
                continue
            return (float(x), float(y), float(z))
        except ValueError:
            print("Invalid syntax")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    resultcenter1 = math.sqrt((pos1[0]**2) + (pos1[1]**2) + (pos1[2]**2))
    print(f"Got a first tuple: ({pos1[0]},{pos1[1]},{pos1[2]})")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: {resultcenter1:.4f}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    resultdistance = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
        )
    print(f"Distance between the 2 sets of coordinates: {resultdistance:.4f}")


if __name__ == "__main__":
    main()
