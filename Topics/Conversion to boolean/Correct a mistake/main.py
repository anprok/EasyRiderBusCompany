def compare(numerator, denominator):
    fraction = 0.5
    return bool(denominator and numerator / denominator == fraction)


a = int(input())
b = int(input())

print(compare(a, b))