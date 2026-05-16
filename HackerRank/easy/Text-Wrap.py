# ============================================
# Problem: Text Wrap
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/text-wrap
# ============================================
# Task:
# Given a long string S and a width w, wrap the string 
# into a paragraph of width w by adding newline characters ('\n').
# ============================================

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)