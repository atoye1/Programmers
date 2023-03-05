import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

c = Counter(cards)

for num in nums:
    if num in c:
        print(c[num], end=' ')
    else:
        print(0, end=' ')