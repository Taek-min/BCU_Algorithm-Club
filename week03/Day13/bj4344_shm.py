num = int(input())
for k in range(num):
    array = list(map(int, input().split()))
    people = array[0]
    sum = 0
    cnt = 0
    perc = 0
    for i in range(1, people + 1):
        sum += array[i]
        avg = float(sum / people)

    for j in range(1, people + 1):
        if avg < array[j]:
            cnt += 1
    perc = (cnt / people) * 100
    print("%.3f%%" %perc)
