n = int(input())
five_count = n // 5
n -= five_count * 5

if n % 2 != 0 and five_count >= 1:
    n += 5
    five_count -= 1
    
if n % 2 != 0:
    print(-1)
else:
    print(int(five_count + n / 2))
