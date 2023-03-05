import sys
N = int(sys.stdin.readline())
members = [sys.stdin.readline().rstrip() for i in range(N)]

# members.sort(key=lambda x: x[2])
members.sort(key=lambda x: int(x.split()[0]))

# print(members)
print('\n'.join(members))
