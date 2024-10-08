"""" Common Methods: keys(), values(), items(), get(), update(), pop(), popitem() """

student_name = {'1':"Red",'2':"Yellow",'3':"Blue"}


# keys()
print(student_name.keys())

# values()
print(student_name.values())

# items()
print(student_name.items())

#get()
keyget = student_name.get("1")
print(keyget)

#update ()
student_name.update({'1':"One",'2':"Two"})
print(student_name)

# metod: pop(): pop specific item
value = student_name.pop('1')
print(f"value:{value}")

print(student_name)

# popitem: pop key and value
items = student_name.popitem()
print(f"item from method popitem:{items}")
print(student_name)

