def calculate_sum(numbers):
    tot=0
    for n in numbers:
        tot+=n
    return tot

def find_min(numbers):
    mn = numbers[0]
    for n in numbers[1:]:
        if n<mn:
            mn=n
    return mn
    
def find_max(numbers):
    mx = numbers[0]
    for n in numbers[1:]:
        if n>mx:
            mx=n
    return mx

a = [6,7,4,2,0]
print(calculate_sum(a), sum(a))
print(find_min(a), min(a))
print(find_max(a), max(a))