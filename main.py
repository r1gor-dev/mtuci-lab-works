def greet(name):
    print("Привет,", name)

def square(num):
    return num**2

def max_of_two(a, b):
    if a>b:
        return a
    return b

greet("Клим")
greet("Матвей")
print(square(4))
print(square(7))
print("10..5", max_of_two(10,5))
print("-3..8", max_of_two(-3,8))