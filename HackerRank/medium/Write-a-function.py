# ============================================
# Problem: Write a Function
# Platform: HackerRank
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/write-a-function
# ============================================
# Task:
# Given a year, determine if it is a leap year
# Leap year conditions:
# - Divisible by 4 AND not divisible by 100
# - OR divisible by 400
# Return True if leap year, False otherwise
# Example: 2000 → True, 1900 → False
# ============================================

def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True 
    return leap

year = int(input())