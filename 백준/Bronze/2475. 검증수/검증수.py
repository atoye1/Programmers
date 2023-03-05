nums = list(map(int, input().split()))
total = 0

for num in nums:
    total += num ** 2
print(total % 10)