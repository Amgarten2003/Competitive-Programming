# Asked by Google
# Coded in 23/04/2022 - April 23, 2022


def solution(a):
    already_seem = {}
    
    for number in a:
        if number in already_seem:
            return number
        already_seem[number] = 1
    
    return -1
