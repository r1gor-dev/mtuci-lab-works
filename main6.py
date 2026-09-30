measurements = (1.2, 3.4, 5.6, 7.8, 9.1, 6.7, 2.2, 3.2)
print(measurements[0], measurements[-1])
print(measurements[1:4])

try:
    measurements[0]=0.1
except TypeError:
    print("Нельзя")

#measurements[0]=0.1

f1,f2 = measurements[:2]
print(f1,f2)
tmp = list(measurements)
tmp[0] = 42.0
measurements = tuple(tmp)
print(measurements)