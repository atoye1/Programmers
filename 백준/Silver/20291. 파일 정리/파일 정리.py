from collections import Counter
num = int(input())
files = [input() for _ in range(num)]
c = Counter()

for _file in files:
    ext = _file.split('.')[1]
    if c.get(ext):
        c[ext] += 1
    else:
        c[ext] = 1

for k, v in sorted(c.items(), key=lambda x: x[0]):
    print(k, v)