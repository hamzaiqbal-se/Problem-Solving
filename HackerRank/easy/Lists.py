# ============================================
# Problem: Lists
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/python-lists
# ============================================
# Task:
# Perform 7 list operations based on commands:
# insert i e, print, remove e, append e,
# sort, pop, reverse
# Example: append 1, append 2, insert 1 3, print → [1,3,2]
# ============================================

if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for i in range(N):
        args = input().split()
        command = args[0]
        
        if command == "insert":
            my_list.insert(int(args[1]), int(args[2]))
            
        elif command == "print": 
            print(my_list)
            
        elif command == "remove":
            my_list.remove(int(args[1]))
            
        elif command == "append":
            my_list.append(int(args[1]))
            
        elif command == "sort":
            my_list.sort()
            
        elif command == "pop":
            my_list.pop()
            
        elif command == "reverse":
            my_list.reverse()    
            
            
            
            
            
