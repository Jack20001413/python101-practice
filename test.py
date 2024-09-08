# All things in Python are considered objects. There are 2 types of objects: mutable & immutable

# Immutable
age = 8
print(id(age))

# A new object is created when an immutable object's value is changed
age += 1
print(id(age))

# Mutable
list = [1, 2]
print(id(list))

# The mutable object retains its ID when its value is changed
list.append(3)
print(id(list))