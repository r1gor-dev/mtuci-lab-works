# name = "игорь"
# age = 18
# height = 1.86
# is_student = True
# print(name, age, height, is_student)  # вывод переменных
# print(type(name), type(age), type(height), type(is_student))  # вывод типов
# # mutable переменные
# age = 81
# is_student = False
# print(age, is_student)

# name = input()
# surname = input()
# agestr = input()
# print(type(agestr))
# age = int(agestr)  # меняем тип
# print(type(age))
# height = float(input())  # сразу получаем дробный рост 
# print(name, surname, age, height)
# print(type(age), type(height))

# a=15
# b=4
# # операции
# print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)
# # смена приоритета операций
# print(2+3*4, (2+3)*4)

# n1 = float(input()); n2 = float(input())
# print(f"{n1} + {n2} = {n1+n2}")
# print(f"{n1} - {n2} = {n1-n2}")
# print(f"{n1} * {n2} = {n1*n2}")
# print(f"{n1} / {n2} = {n1/n2}")

# print("1-10: ")
# for i in range(1,10+1):
#     print(i, end=" ")
# print()
# print("10-1:")
# for i in range(10,0,-1):
#     print(i, end=" ")
# print()
# print("n%2==0, 0-20:")
# for i in range(0,20+1,2):
#     print(i, end=" ")
# print()
# print("n%3==0, 0-15:")
# for i in range(0,15+1,3):
#     print(i, end=" ")

# n = int(input())
# totsum=0
# for i in range(1,n+1):
#     totsum+=i
# print(n, totsum)

# cnt=10
# while cnt>0:
#     print(cnt, end=" ")
#     cnt-=1
# print()
# print("Цикл завершён")

# from math import *
# r = 5.0
# c = 2*pi*r
# s=pi*(r**2)
# print(r,c,s)
# n=144
# print(n, sqrt(n))

# n =int(input())
# if n>0: print("Positive Hack Days")
# elif n<0: print("Negative Hack Days")
# else: print("ZERO")

# if n%2==0: print("Even boozer")
# else: print("Odd boozer")

# age = int(input())
# has_access = True
# print(f"Допуск имеется: {has_access}")
# print(f"{"Доступ разрешён" if age > 17 and has_access else "Доступ запрещён"}") 

n=int(input())
totsum=0.0
for _ in range(n):
    val = float(input())
    totsum+=val
if n>0:  # ZeroDivisionError
    avg=totsum/n
    print(totsum, avg)
else:
    print("Нет чисел для операции")