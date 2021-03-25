list_A = []
list_B = []
for i in range(10):
    list_A.append(int(input()) % 42) # 나머지를 이제 list_A에 집어넣음.

for j in list_A:                     # 리스트 B에 없는 값을 넣어버림.
    if j not in list_B :             # 이걸로 중복이 되는걸 없앰.
        list_B.append(j)

print(len(list_B))              
