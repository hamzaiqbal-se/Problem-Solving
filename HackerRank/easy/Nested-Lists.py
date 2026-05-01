# ============================================
# Problem: Nested Lists
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/nested-list
# ============================================
# Task:
# Given names and grades of N students, store in nested list
# Print name(s) of student(s) with second lowest grade
# If multiple students have same second lowest grade,
# print names alphabetically, each on a new line
# Example: [["chi",20.0],["beta",50.0],["alpha",50.0]] → alpha, beta
# ============================================

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])  
         
    sorted_score = sorted(set([x[1] for x in students]))
    second_lowest_score = sorted_score[1]
    final_names = [x[0] for x in students if x[1]== second_lowest_score]
    final_names.sort()
    for name in final_names:
        print(name)
