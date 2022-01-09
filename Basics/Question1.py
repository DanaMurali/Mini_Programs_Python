# Print the result of the multiplication of two sets of integers if it is less than 1000. If the result is greater than 1000, print their sum.

def multiplication_or_addition(num1, num2):
    product = num1 * num2 

    if product < 1000:
        return product
    else:
        return num1 + num2

result = multiplication_or_addition(25,26)
print(result)
# 650

result = multiplication_or_addition(120, 123)
print(result)
# 243