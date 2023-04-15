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

keys_list = list(c.keys())
keys_list.sort()
for key in keys_list:
    print(key, c[key], sep=' ')