import sys

n = int(sys.stdin.readline())
candidates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
candidates.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for time in candidates:
    if time[0] > time[1]:
        continue
    # 시작시간이 현재 종료시간보다 크거나 같으면, 회의할 수 있다.
    if time[0] >= end_time:
        count += 1
        end_time = time[1]

print(count)
