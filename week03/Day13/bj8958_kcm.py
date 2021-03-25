num = int(input())

for i in range(num):
    list_N = list(input())
    sum = 0
    count = 1
    for j in range(len(list_N)):
        if list_N[j] == "X":
            count = 1
            continue
        sum += count
        count += 1
    print(sum)
