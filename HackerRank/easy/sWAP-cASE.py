# ============================================
# Problem: sWAP cASE
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/swap-case
# ============================================
# Task:
# Given a string, swap all lowercase to uppercase
# and uppercase to lowercase
# Example: "Www.HackerRank.com" → "wWW.hACKERrANK.COM"
# ============================================

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)