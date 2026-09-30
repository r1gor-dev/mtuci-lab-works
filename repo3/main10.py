def analyze(numbers):
    xmn = min(numbers)
    xmx = max(numbers)
    xavg = sum(numbers)/len(numbers)
    return xmn, xmx, xavg

a = [1,2,3,4,5]
mn, mx, avg = analyze(a)

print(mn, mx, avg)