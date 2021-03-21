def d(num):
    N = num + (num // 10**3) + ((num // 10**2) % 10) + ((num // 10) % 10) + (num % 10)
    if N <= 10000:
        return N

array = []
fix_num = []
for i in range(10000):
    fix_num.append(d(i))
    array.append(i)
self_num = list(set(array) - set(fix_num))
self_num.sort()

for j in self_num:
    print(j)