def range_sum(numbers, start, end):
    res = 0
    for i in numbers:
        if start <= i <= end:
            res += i
    return res


input_numbers = list(map(int, input().split(" ")))
a, b = list(map(int, input().split(" ")))
print(range_sum(input_numbers, a, b))