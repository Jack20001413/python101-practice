def range_extract(args):
    result = ""
    current = 0

    while current < len(args):
        start = args[current]
        while current < len(args) - 1 and args[current] + 1 == args[current + 1]:
            current += 1
        end = args[current]
        if end - start >= 2:
            result += f"{start}-{end},"
        elif end - start == 1:
            result += f"{start},{end},"
        else:
            result += f"{end},"
        current += 1
    return result.rstrip(",")

num_list = [-6,-3,-2,-1,2,10,15,16,18,19,20]
ranges = range_extract(num_list)
print(ranges)

