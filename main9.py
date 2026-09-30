def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

a = [1,2,3,4,5]
print(find_element(a,67))
print(find_element(a,5))
