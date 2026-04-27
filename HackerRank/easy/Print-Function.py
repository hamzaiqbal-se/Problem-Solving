# ============================================
# Problem: Print Function
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/python-print
# ============================================
# Task:
# Given integer n, print all integers from 1 to n
# as a single string without spaces
# Example: n=5 → 12345
# ============================================

if __name__ == '__main__':
    n = int(input().strip())
    
    for i in range(1, n + 1):
        print(i, end="")