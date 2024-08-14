set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_difference_set = set1 ^ set2

even_numbers = {x for x in range(1, 11) if x % 2  0}

# Example 1: Working with dictionaries

# Creating a dictionary of student grades 
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 95}

# Accessing values using keys 
print("Bob's grade:", grades['Bob']) # Output: Bob's grade: 92

# Adding a new entry 
grades['Eve'] = 90

# Iterating through keys and values
for student, grade in grades.items():
     print(f"{student}: {grade}")

# Using get() method to avoid KeyError
print("Frank's grade:", grades.get('Frank', 'Grade not found')) # Output: Frank's grade: Grade not found


# Example 2: Set operations

set1 = {1, 2, 3, 4, 5} 
set2 = {3, 4, 5, 6, 7}

# Union of two sets

union_set = set1 | set2
print("Union set:", union_set) # Output: Union set: {1, 2, 3, 4, 5, 6, 7}

# Intersection of two sets

intersection_set = set1 & set2
print("Intersection set:", intersection_set) # Output: Intersection set: {3, 4, 5}

# Difference between two sets
difference_set = set1 - set2
print("Difference set (set1 - set2):", difference_set) # Output: Difference set (set1 set2): {1, 2}

# Symmetric difference between two sets
symmetric_difference_set = set1 ^ set2
print("Symmetric difference set:", symmetric_difference_set) # Output: Symmetric difference set: {1, 2, 6, 7}


# Example 4: Set operations and methods

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Adding elements to a set
set1.add(5)

# Removing elements from a set 
set2.discard(6)

# Checking subset and superset
print("Is set1 a subset of set2?", set1.issubset(set2)) # Output: Is set1 a subset of set2? False
print("Is set2 a superset of set1?", set2.issuperset (set1)) # Output: Is set2 a superset of set1?True


# Example 5: Using sets for unique operations

# Finding unique elements from multiple lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

unique_elements = set(list1).union(set(list2)).difference(set(list3))
print("Unique elements:", unique_elements) # Output: Unique elements: {1, 2}


# Given a list of student grades, calculate the average grade for each student and store them in a dictionary.

grades = {'Alice': [85, 90, 92], 'Bob': [88, 87, 85], 'Charlie': [90, 91, 89]} 
average_grades = {}

for student, grade_list in grades.items(): 
     average_grades[student] = sum(grade_list) / len(grade_list)

print("Average Grades:", average_grades)