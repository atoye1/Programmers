import sys
N = int(sys.stdin.readline())
members = [sys.stdin.readline().rstrip().split() + [i] for i in range(N)]

members.sort(key=lambda x: x[2])
members.sort(key=lambda x: int(x[0]))

for elem in members:
    print(' '.join(elem[:2]))
