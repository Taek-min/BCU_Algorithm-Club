num = int(input())

for i in range(num):
    list_N = list(map(int,input().split()))
    Sum = 0
    count = 0

    for j in range(1,len(list_N)):
        Sum += list_N[j]

    avg = Sum / list_N[0]

    for t in range(1,len(list_N)):
        if avg < list_N[t]:
            count += 1

    avg = count / (len(list_N)-1) * 100
    print("%.3f%%" %avg)
