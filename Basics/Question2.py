# Iterate from the start number to the end number of the first 10 numbers, and In each iteration print the sum of the current number with the previous number

def sum_num (num):
    previous_num = 0 

    for number in range(num):
        sum = previous_num + number

        print("Current Num: ", number, "Previous Num: ", previous_num, "Sum: ", sum)

        previous_num = number

sum_num(10)

# ('Current Num: ', 0, 'Previous Num: ', 0, 'Sum: ', 0)
# ('Current Num: ', 1, 'Previous Num: ', 0, 'Sum: ', 1)
# ('Current Num: ', 2, 'Previous Num: ', 1, 'Sum: ', 3)
# ('Current Num: ', 3, 'Previous Num: ', 2, 'Sum: ', 5)
# ('Current Num: ', 4, 'Previous Num: ', 3, 'Sum: ', 7)
# ('Current Num: ', 5, 'Previous Num: ', 4, 'Sum: ', 9)
# ('Current Num: ', 6, 'Previous Num: ', 5, 'Sum: ', 11)
# ('Current Num: ', 7, 'Previous Num: ', 6, 'Sum: ', 13)
# ('Current Num: ', 8, 'Previous Num: ', 7, 'Sum: ', 15)
# ('Current Num: ', 9, 'Previous Num: ', 8, 'Sum: ', 17)