# ============================================
# Problem: String Split and Join
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/python-string-split-and-join
# ============================================
# Task:
# Given a string, split on space delimiter
# then join using hyphen "-"
# Example: "this is a string" → "this-is-a-string"
# ============================================

def split_and_join(line):
    split_str = line.split(" ")
    join_str = "-".join(split_str)
    return join_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)