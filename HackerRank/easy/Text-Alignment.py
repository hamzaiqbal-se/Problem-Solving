# ============================================
# Problem: Text Alignment (HackerRank Logo)
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/text-alignment
# ============================================
# Task:
# Replace the blanks (______) with rjust, ljust, or center 
# to create the HackerRank logo of variable thickness.
# - ljust(width): Left align
# - rjust(width): Right align
# - center(width): Center align
# ============================================

if __name__ == '__main__':
    thickness = int(input()) # This must be an odd number
    c = 'H'

    # 1. Top Cone
    # Uses rjust and ljust to push 'H' towards the center
    for i in range(thickness):
        print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

    # 2. Top Pillars
    # Uses center to align the pillars within their specific widths
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    # 3. Middle Belt
    # Centered to bridge the gap between pillars
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    # 4. Bottom Pillars
    # Same logic as Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

    # 5. Bottom Cone
    # Inner alignment creates the cone, outer rjust pushes it to the far right
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))