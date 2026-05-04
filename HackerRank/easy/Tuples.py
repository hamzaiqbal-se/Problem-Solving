# ============================================
# Problem: Tuples
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/python-tuples
# ============================================
# Task:
# Given n integers, create a tuple t of those integers
# Compute and print hash(t)
# Note: hash() is a built-in function, no import needed
# Example: n=2, integers=1 2 → hash((1,2))
# ============================================

if __name__=='__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
