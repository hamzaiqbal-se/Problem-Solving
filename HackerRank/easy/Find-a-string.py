# ============================================
# Problem: Find a String
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/find-a-string
# ============================================
# Task:
# Given a string and a substring, count how many
# times the substring occurs in the string
# Traversal left to right, case-sensitive
# Example: "ABCDCDC", "CDC" → 2
# ============================================

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)