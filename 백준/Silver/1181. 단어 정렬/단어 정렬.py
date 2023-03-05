import sys
N = int(sys.stdin.readline().rstrip())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

words = list(set(words))
words.sort()
words.sort(key=len)

print('\n'.join(words))