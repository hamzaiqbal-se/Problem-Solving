# ============================================
# Problem: Python If-Else
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/py-if-else
# ============================================
# Task:
# If n is odd → print "Weird"
# If n is even and between 2-5 → print "Not Weird"
# If n is even and between 6-20 → print "Weird"
# If n is even and > 20 → print "Not Weird"
# ============================================

import math
import os
import random
import re
import sys


n = int(input().strip())
if n%2!=0:
    print('Weird')
else:
    if 2<= n <=5:
        print('Not Weird')
    elif 6<= n<=20:
        print('Weird')
    elif n>20:
        print('Not Weird')