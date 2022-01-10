# Write code to extract each digit from the integer, in the reverse order

integer = 123456789

while (integer > 0):
    digit = integer % 10
    integer = integer // 10

    print(digit)
