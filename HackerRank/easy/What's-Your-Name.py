# ============================================
# Problem: What's Your Name?
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/whats-your-name
# ============================================
# Task:
# Given firstname and lastname on two separate lines
# Print: "Hello firstname lastname! You just delved into python."
# Example: "Hello Harry Potter! You just delved into python."
# ============================================

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)