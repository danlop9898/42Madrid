#!/usr/bin/env python3

def main() -> None:
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    print("Plant:", name)
    print("Height:", str(height) + "cm")
    print("Age:", str(age) + " days")
    print("=== End of Program ===")

# Sirve para que se ejecute como programa principal y no se ejecuta
#  automaticamente si se importa dese otro lado


if __name__ == "__main__":
    main()
