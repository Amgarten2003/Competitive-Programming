# Asked by Amazon
# Coded in 23/04/2022 - April 23, 2022


def solution(s):
    for char in s:
        if s.index(char) == s.rindex(char):
            return char
    
    return '_'

print(solution('abacabaabacaba'))
