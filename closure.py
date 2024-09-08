# Closure is a function that remembers values in enclosing scopes even if they are not active anymore

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

increment = counter()

print(increment()) #1
print(increment()) #2
print(increment()) #3