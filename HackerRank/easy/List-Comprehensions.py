# ============================================
# Problem: List Comprehensions
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/list-comprehensions
# ============================================
# Task:
# Given x, y, z and n, print all [i,j,k] coordinates
# on a 3D grid where i+j+k != n
# 0 <= i <= x, 0 <= j <= y, 0 <= k <= z
# Use list comprehensions only
# Example: x=1,y=1,z=2,n=3 → [[0,0,0],[0,0,1]...]
# ============================================

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    output = [[i, j, k] for i in range(x + 1)
                        for j in range(y + 1)
                        for k in range(z + 1)
                        if (i + j + k) != n]
    print(output)