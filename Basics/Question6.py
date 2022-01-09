# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

list = [10, 20, 33, 46, 55, 77, 105, 204, 335]

def divisible_by_five (num):
   
    for number in num:
        if number % 5 == 0:
            print(number)

divisible_by_five(list)    