N = int(input())
coords = []
for _ in range(N):
    x, y = map(int, input().split())
    coords.append([x, y])
coords.sort(key=lambda x: [x[1], x[0]])

for coord in coords:
    print(coord[0], coord[1], sep=' ')
