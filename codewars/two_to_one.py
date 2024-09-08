from operator import concat

def longest_two_to_one(string1, string2):
    # concatenated_string = sorted(set(concat(string1, string2).lower()))
    # return  ''.join(concatenated_string)
    return ''.join(sorted(set(string1 + string2)))

string1 = 'aretheyhere'
string2 = 'yestheyarehere'

result = longest_two_to_one(string1, string2)
print(result)