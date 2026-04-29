# ============================================
# Problem: Find the Runner-Up Score!
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
# ============================================
# Task:
# Given n scores, find the runner-up (second highest) score
# Store scores in a list, remove duplicates, sort and get second max
# Example: [2,3,6,6,5] → runner-up = 5
# ============================================

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_score = set(arr)
    sorted_array = sorted(unique_score)
    print(sorted_array[-2])