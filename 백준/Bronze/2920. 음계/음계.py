melodies = list(map(int, input().split()))
answer = 'mixed'
if melodies[0] == 1:
    for i in range(7):
        answer = 'ascending'
        if melodies[i] == melodies[i + 1] - 1:
            continue
        else:
            answer = 'mixed'
            break
elif melodies[0] == 8:
    answer = 'descending'
    for i in range(7):
        if melodies[i] == melodies[i + 1] + 1:
            continue
        else:
            answer = 'mixed'
            break
print(answer)
