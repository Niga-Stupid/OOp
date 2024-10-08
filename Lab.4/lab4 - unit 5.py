# Slide Unit 5 page 13, 14, 15,16, 18, 20
# เปิดไฟล์ Slide Unit 5 เขียนโค้ดโปรแกรมหน้าที่ 13, 14, 15, 16, 18, 20

"""" Common Metthods: 
append(), extend(), insert()
remove(), pop(), index()
count(), sort(), reverse()
"""
# test use funtions method

# Define list
list = [1, 2, 4, 3, 5]

# append(): add one elements in to list
list.append(6)
print("List after append:", list)

# extend(): add more elements in to list
list.extend([7,8])
print("List after extend:", list)

# insert(): Can define data to index and element 
list.insert(1,20)
print("List after insert[1]: 20:", list)

# remove(): Delete the data completely.
list.remove(20)
print("List after remove 20:", list)

# pop(): pop data Last in - Frist Out
pop_data = list.pop()
print("List after pop:", list)
print("Pop value:", pop_data)

# index(): Find the value data in index
print("Value 4 in index:", list.index(4))

# count(): count value you want in list
print("List after count(2):", list.count(2))

# sort()
list.sort()
print("List after Sort:", list)

# reverse()
list.reverse()
print("List after Reverse:", list)
