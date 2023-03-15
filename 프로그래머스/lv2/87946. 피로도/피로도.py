from itertools import permutations 

def solution(k, dungeons):
    # 최댓값을 구해야하므로 최대 던전 개수부터 시작해서 내려간다.
    # 중간에 만족하는 값이 나오면 바로 리턴해주면 된다.
    for i in range(len(dungeons), 0, -1):
        # 8개, 7개, 6개, ... 식으로 순열을 구해 내려간다.
        for cases in permutations(dungeons, i):
            # 현재 피로도를 리셋한다.
            now = k
            passed = True
            for case in cases:
                if now < case[0]:
                    passed = False
                    break
                else:
                    now -= case[1]
            if passed:
                return i