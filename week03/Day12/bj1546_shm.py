num = int(input())
subject= sorted(list(map(int, input().split())), reverse= True)
M = subject[0]
new_sum = 0

for i in range(len(subject)):
    new_sum += subject[i]/M*100


new_score = float(new_sum / len(subject))

print(new_score)
