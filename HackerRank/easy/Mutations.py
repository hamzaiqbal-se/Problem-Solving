# ============================================
# Problem: Mutations
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/python-mutations
# ============================================
# Task:
# Given an immutable string, change character at
# given position by converting to list, mutating,
# then joining back
# Example: "abracadabra", position=5, char="k" → "abrackdabra"
# ============================================

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)