def highestPlace(seq):
    winScore = max(seq)
    isWinnerPassed = False
    bestScore = -1
    for i in range(len(seq) - 1):
        if seq[i] % 10 == 5 and isWinnerPassed and seq[i + 1] < seq[i] and seq[i] > bestScore:
            bestScore = seq[i]
        if seq[i] == winScore:
            isWinnerPassed = True
    if bestScore == -1:
        return 0

    count = 0
    for n in seq:
        if n > bestScore:
            count += 1
    return count + 1

n = int(input())
l = list(map(int, input().split(' ')))
print(highestPlace(l))
