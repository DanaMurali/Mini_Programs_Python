# Given two list of numbers, create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

list1 = [10, 20, 23, 11, 17, 44, 55]
list2 = [13, 43, 24, 36, 12, 33, 66]

def merge_list(list_one, list_two):
    new_list = []
    
    for num in list_one: 
        if num % 2 != 0:
            new_list.append(num)

    for num in list_two:
        if num % 2 == 0:
            new_list.append(num)
    
    return new_list
            
print(merge_list(list1, list2))          

