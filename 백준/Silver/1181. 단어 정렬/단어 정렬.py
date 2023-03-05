import sys
N = int(sys.stdin.readline().rstrip())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
