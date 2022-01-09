#  Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def remove_characters(string, num):
    return string[num:]

print(remove_characters("goodbye", 4)) 