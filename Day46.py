def octal_to_decimal(octal):
    decimal = 0
    power = 0
    while octal > 0:
        decimal += (octal % 10) * (8 ** power)
        octal //= 10
        power += 1
    return decimal

octal_number = int(input("Enter an octal number: "))

decimal_number = octal_to_decimal(octal_number)

print(f"The decimal equivalent of {octal_number} is {decimal_number}")
