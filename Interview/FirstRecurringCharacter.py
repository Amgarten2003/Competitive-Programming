# Asked by Google
# Coded in 23/04/22 - April 23, 2022


def first_recurring_character(characters):
    counts = {}

    for char in characters:
        if char in counts:
            return char
        counts[char] = 1
    
    return None
