N = input()
idx = 0
answer = 0
for c in N:
    if idx < len(N) // 2:
        answer += int(c)
    else:
        answer -= int(c)
    idx += 1
result = 'LUCKY' if answer == 0 else 'READY'
print(result)
