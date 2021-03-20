array = []
cnt = 0
for i in range(10):
    num = int(input())
    new = num % 42 
    array.append(new)       # 여기까지 나머지를 array배열에 넣는것


for j in range(9):         # 중복되는지 확인. 
   for k in range(1, 10):
        if k > j:
            if array[j] == array[k]:
                j = k - 1
                cnt += 1
                break

print(10 - cnt)