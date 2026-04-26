# ============================================
# Problem: Python: Loop
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/python-loops
# ============================================
# Task:
# Given integer n, for all non-negative integers i < n
# print the square of each number (i*i) on a separate line
# Example: n=3 → 0, 1, 4
# ============================================

if __name__ == '__main__':
    n = int(input().strip())
    for i in range(n):
        print(i**2)
