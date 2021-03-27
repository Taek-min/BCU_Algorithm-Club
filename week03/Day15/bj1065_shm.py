def han_num(N):      
    cnt = 0
    if (N < 100):
        for i in range(1, N + 1):
            cnt += 1
        return cnt
    else:
        for j in range(100, N + 1):        
            A = j % 10              # 첫째 자리
            B = (j // 10) % 10      # 둘째 자리
            C = j // 100            # 셋째 자리
            if A - B == B - C:
                cnt += 1 
        return (99 + cnt)

N = int(input())
print(han_num(N))


