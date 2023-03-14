n = list(input())
last = False
counter = {'0': 0, '1': 0}
while n:
    curr = n.pop()
    if curr != last:
        counter[curr] += 1
        last = curr
print(min(counter['0'], counter['1']))