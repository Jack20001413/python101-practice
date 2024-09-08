# This function has to apply additional set() for better performance. Value returned by set() function 
# will be iterated over to count the appearance of each number instead of iterating over the original number list
def find_uniq(array):
    num_set = set(array)
    n = [num for num in num_set if array.count(num) == 1][0]
    return n

def find_uniq2(array):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

arr = [ 0, 0, 0.55, 0, 0 ]
result = find_uniq2(arr)
print(result)