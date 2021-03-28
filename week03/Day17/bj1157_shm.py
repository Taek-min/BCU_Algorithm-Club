WORD = str(input().upper())
comp = list(set(WORD))
array = []

for i in comp:
    array.append(WORD.count(i))

if array.count(max(array)) > 1:
    print("?")
else:
    cnt = array.index(max(array))
    print(comp[cnt])
    