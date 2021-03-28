T = int(input())
for i in range(T):
    R, S = list(map(str, input().split()))
    for j in S:
        P = j * int(R)
        print(P, end ="")
    print("")