import sys

# x, y간의 가중치를 정수로 변환
def convert(s):
    x, y = s.split()
    return int(y) + int(x)/1000000


arr = sys.stdin.readlines()[1:]
arr = sorted(arr, key=lambda x: convert(x))  # 변환한 가중치로 정렬함.
print(''.join(arr))  # print함수를 여러번 호출하면 성능상 안좋음
