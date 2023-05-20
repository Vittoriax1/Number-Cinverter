def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_hex(decimal):
    return hex(decimal)[2:]

def hex_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

while True:
    print("Number Conversion")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Hexadecimal")
    print("4. Hexadecimal to Decimal")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        decimal = int(input("Enter a decimal number: "))
        binary = decimal_to_binary(decimal)
        print("Binary: " + binary)
        print()
        
    elif choice == "2":
        binary = input("Enter a binary number: ")
        decimal = binary_to_decimal(binary)
        print("Decimal: " + str(decimal))
        print()
        
    elif choice == "3":
        decimal = int(input("Enter a decimal number: "))
        hexadecimal = decimal_to_hex(decimal)
        print("Hexadecimal: " + hexadecimal)
        print()
        
    elif choice == "4":
        hexadecimal = input("Enter a hexadecimal number: ")
        decimal = hex_to_decimal(hexadecimal)
        print("Decimal: " + str(decimal))
        print()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.\n")
