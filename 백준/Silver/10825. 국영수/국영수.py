import sys
input = sys.stdin.readline

n = int(input())
scores = [input().split() for _ in range(n)]

scores.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
print('\n'.join([x[0] for x in scores]))
