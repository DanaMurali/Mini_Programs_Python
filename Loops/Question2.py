# Print the following pattern

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

print("The Pattern is as follows:")

last_num = 6

for row in range(1, last_num):
    for column in range(1, row + 1):
        print(column, end=" ")
    print(" ")