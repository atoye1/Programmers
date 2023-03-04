import sys
n = int(sys.stdin.readline())
ropes = []

for i in range(n):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

curr_weight = ropes[0]
count = 1

for rope in ropes[1:]:
    count += 1
    new_weight = rope * count
    if new_weight > curr_weight:
        curr_weight = new_weight

print(curr_weight)