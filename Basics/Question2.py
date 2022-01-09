# Iterate from the start number to the end number of the first 10 numbers, and In each iteration print the sum of the current number with the previous number

def sum_num (num):
    previous_num = 0 

    for number in range(num):
        sum = previous_num + number

        print("Current Num: ", number, "Previous Num: ", previous_num, "Sum: ", sum)

        previous_num = number

sum_num(10)