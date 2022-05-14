def solution(s):
    for char in s:
        if s.index(char) == s.rindex(char):
            return char
    
    return '_'

print(solution('abacabaabacaba'))