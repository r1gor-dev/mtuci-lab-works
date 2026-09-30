def calculate_average(measurements):
    tot=0; cnt=0
    for i in measurements:
        tot+=i; cnt+=1
    return tot / cnt if cnt>0 else 0


def find_minimum(measurements):
    mn = measurements[0]
    for i in measurements[1:]:
        if i<mn:
            mn=i
    return mn

def find_maximum(measurements):
    mx = measurements[0]
    for i in measurements[1:]:
        if i>mx:
            mx=i
    return mx

def count_above_average(measurements):
    avg = calculate_average(measurements)
    cnt=0
    for i in measurements:
        if i>avg:
            cnt+=1
    return cnt

def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1

def analyze_measurements(measurements):
    return (find_minimum(measurements),
            find_maximum(measurements),
            calculate_average(measurements))

df = [1.23, 4.32, 6.73, 8.19, 3.62, 4.18, 3.52, 6.66, 1.21, 3.22]
target=3.52
mn, mx, avg = analyze_measurements(df)
print(len(df))
print(mn)
print(mx)
print(avg)
print(count_above_average(df))

if find_value(df,target) != -1:
    print(f"Нашлось {target} на {find_value(df,target)}")
else:
    print(f"{target} в датафрейме не нашлось. :(")