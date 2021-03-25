num = int(input())
list_N = list(map(int,input().split()[:num]))
Max = max(list_N)


for i in range(num):
    list_N[i] = list_N[i] / Max * 100


print(sum(list_N) / num)
    



