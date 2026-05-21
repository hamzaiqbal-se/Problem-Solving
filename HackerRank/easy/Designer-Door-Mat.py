# ============================================
# Problem: Designer Door Mat
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/designer-door-mat
# ============================================
# Task:
# Design a door mat of size N x M (M = 3 * N) with 'WELCOME' 
# written in the center using string formatting methods.
# The design pattern must only use '|', '.' and '-' characters.
# ============================================

if __name__ == '__main__':
    # N is the height (must be an odd number) and M is the width (3 times N)
    N, M = map(int, input().split())

    # The design element that repeats
    pattern = '.|.'

    # 1. Top Part (Before WELCOME)
    # Generates the upper pyramid. Pattern increases as: 1, 3, 5...
    for i in range(N // 2):
        print((pattern * (2 * i + 1)).center(M, '-'))
        
    # 2. Middle Part (WELCOME Line)
    # Perfectly centered horizontally within the width M
    print('WELCOME'.center(M, '-'))

    # 3. Bottom Part (After WELCOME)
    # Generates the inverted pyramid by running the loop in reverse order
    for i in range(N // 2 - 1, -1, -1):
        print((pattern * (2 * i + 1)).center(M, '-'))