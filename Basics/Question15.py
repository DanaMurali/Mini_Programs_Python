# Write a function called exponent(base, exp) that returns an int value of base raised to the power of exp.

def exponent(base, exp):
    int = base**exp
    print(int)

exponent(2,2)
# 4

def exponent(base, exp):
    num = exp
    result = 1

    while num > 0:
        result = result * base
        num = num - 1

    print(base, "raised to the power of", exp, "is", result)


exponent(5, 3)

