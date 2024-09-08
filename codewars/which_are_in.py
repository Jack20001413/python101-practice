# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

def in_array(arr1, arr2):
    filter_substrings = set(arr1.copy())
    for word1 in set(arr1):
        count = 0
        for word2 in arr2:
            if word2.find(word1) != -1:
                count += 1
        if count == 0:
            filter_substrings.remove(word1) 
    return sorted(filter_substrings)

def solution2(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

array1, array2 = ["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]
# array1, array2 = ["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]
result = in_array(array1, array2)
print(result)