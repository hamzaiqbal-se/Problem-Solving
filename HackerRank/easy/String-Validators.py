# ============================================
# Problem: String Validators
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/string-validators
# ============================================
# Task:
# Given a string, check if it has at least one:
# - Alphanumeric character (isalnum)
# - Alphabetical character (isalpha)
# - Digit (isdigit)
# - Lowercase letter (islower)
# - Uppercase letter (isupper)
# Print True/False for each on a separate line
# ============================================

if __name__ == '__main__':
    s = input()
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))