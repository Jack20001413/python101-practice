def solution(s):
    sorted_string = sorted(s.lower()).count()
    count = 0
    last_index = len(sorted_string) - 1
    for i in range (1, last_index):
        next_index = i + 1
        previous, current, next = sorted_string[i - 1], sorted_string[i], sorted_string[i + 1]
        # (current == next) and (next_index == last_index) evaluates duplicates happening in the last index of the sorted string
        if ((previous == current) and (next != current)) or ((current == next) and (next_index == last_index)):
            count += 1
    return count

# Another way
def count_duplicates(text):
    return len([c for c in set(text.lower()) if text.lower().count(c)>1])

s = 'abcde'
print(solution(s)) # 0

s = 'oP1N8fikS1MvGmlIPqyL12KPQC6wb3GrTrjmynq98X'
print(solution(s)) # 12

s = 'q8shALnhsdhk84S3l129pkUA7'
print(solution(s)) # 6