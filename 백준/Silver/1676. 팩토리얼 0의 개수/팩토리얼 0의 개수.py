N = int(input())
c_2 = 0
c_5 = 0

# 1부터 N까지 모든 수를 for 순회
for n in range(1, N+1):
    # n을 소인수분해 했을 때, 2의 개수를 카운팅
    while True:
        if n % 2 == 0:
            n /= 2
            c_2 += 1
        else:
            break
    
    # n에서 x2를 다 빼내고 남은 수에 대해 5의 개수를 카운팅
    while True:
        if n % 5 == 0:
            n /= 5
            c_5 += 1
        else:
            break

# 2의 차수와 5의 차수 중 작은 것을 선택, 그 수만큼이 10이 포함된 개수이자 0의 개수이다.
print(min(c_2, c_5))