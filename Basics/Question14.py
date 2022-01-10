# Print downward Half-Pyramid Pattern with Star (asterisk)

for i in range(9, 0, -1):
    for j in range(0, i-1):
        print("*", end=" ")
    print(" ")