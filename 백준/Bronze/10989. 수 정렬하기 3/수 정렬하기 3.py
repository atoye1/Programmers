import sys
input = sys.stdin.readline
n = int(input())
c = [0] * 10001  # 배열을 딕셔너리처럼 사용하면 더 빠르다.

for _ in range(n):
    input_num = int(input())
    c[input_num] += 1

for i in range(1, 10001):
    count = c[i]
    if count:
        for _ in range(count):
            print(i)