# Accept a list of numbers and the size of the list as an input from the user

float_numbers = []

list_size = int(input("Enter the list size: "))

for i in range(0, list_size):
    print("Enter number at location", i, ":")

    item = float(input())
    float_numbers.append(item)

print("The user list is:", float_numbers)