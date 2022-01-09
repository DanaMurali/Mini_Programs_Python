# Given a list of numbers, return True if first and last number of a list is same

list1 = [10, 20, 30, 40, 10]
list2 = [10, 20, 30, 40, 50]

def first_and_last(list):
    if list[0] == list[-1]:
        return True
    else:
        return False

print(first_and_last(list1))            
print(first_and_last(list2))            