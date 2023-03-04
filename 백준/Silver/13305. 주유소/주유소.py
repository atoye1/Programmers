n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
result = 0
for i in range(n - 1):
    if prices[i] < prices[i + 1]:
        prices[i + 1] = prices[i]
# print(prices)

for i in range(n - 1):
    result += distances[i] * prices[i]

print(result)