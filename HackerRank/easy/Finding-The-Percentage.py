# ============================================
# Problem: Finding the Percentage
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/finding-the-percentage
# ============================================
# Task:
# Given a dictionary of student name:[marks]
# Find the average marks of the queried student
# Print average with exactly 2 decimal places
# Example: beta → [30,50,70] → (30+50+70)/3 = 50.00
# ============================================

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    average = sum(marks)/len(marks)
    print(f"{average:.2f}")
    
