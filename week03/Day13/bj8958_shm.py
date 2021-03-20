num = int(input())
for i in range(num):
    quiz = list(str(input()))
    O_score = 0
    X_score = 0
    total = 0
    for j in range(len(quiz)):
        if quiz[j] == 'O':
            O_score += 1
            total += O_score
        else:
            O_score = 0
            X_score = 0
    print(total)
