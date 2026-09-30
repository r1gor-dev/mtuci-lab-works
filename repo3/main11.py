numbers = [-10, 3, -2, 8, -5]

justsort = sorted(numbers)
abssort = sorted(numbers, key=lambda x: abs(x))

print(justsort)
print(abssort)