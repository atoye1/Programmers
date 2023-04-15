times = int(input())
records = [list(map(int, input().split())) for _ in range(times)]

memo = [-1] * (times + 1)
result = 0
for record in records:
    cow_id, cow_pos = record
    if memo[cow_id] == -1:
        memo[cow_id] = cow_pos
    elif memo[cow_id] != cow_pos:
        result += 1
        memo[cow_id] = cow_pos
print(result)
