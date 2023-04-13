L = int(input())
S = list(input())

r = 31
M = 1234567891
total = 0


def getNum(c):
    return ord(c) - ord('a') + 1


for idx, c in enumerate(S):
    num = getNum(c)
    num = num * (r ** idx)
    total += num
print(total % M)
