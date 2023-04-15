seed_money = int(input())
prices = list(map(int, input().split()))

seed1 = seed_money
seed2 = seed_money
stock1 = 0
stock2 = 0

# 시뮬레이션이므로 각각의 상황에 맞게 시뮬레이션을 돌린다.
# 마지막 날은 자산변동과 관계없으니 고려하지 않아도 된다.
for price in prices[:-1]:
    buyable = seed1 // price
    if buyable:
        seed1 -= price * buyable
        stock1 += buyable
asset1 = seed1 + stock1 * prices[-1]

for idx, price in enumerate(prices[:-1]):
    if idx < 3:
        continue
    if prices[idx - 3] < prices[idx - 2] and prices[idx - 2] < prices[idx - 1]:
        # 가격이 3일 연속 상승하였으므로 팔아야된다.
        seed2 += stock2 * price
        stock2 = 0
    elif prices[idx - 3] > prices[idx - 2] and prices[idx - 2] > prices[idx - 1]:
        # 가격이 3일 연속 하락하였으므로 사야한다.
        amount = seed2 // price
        stock2 += amount
        seed2 -= amount * price

asset2 = seed2 + stock2 * prices[-1]

if asset1 == asset2:
    print("SAMESAME")
elif asset1 > asset2:
    print("BNP")
else:
    print('TIMING')
