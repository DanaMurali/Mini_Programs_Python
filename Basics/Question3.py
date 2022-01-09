# In a string, display the characters at the even indices

def even_indices(string):
    # start point = 0, end point = length of string
    # step is going to be 2 because we want even indices.
    # string[character] - specifies the character at specific index.
    for character in range(0, len(string), 2):
        print("Index[", character, "]", string[character])

string = "goodbye"

even_indices(string)

# ('Index[', 0, ']', 'g')
# ('Index[', 2, ']', 'o')
# ('Index[', 4, ']', 'b')
# ('Index[', 6, ']', 'e')