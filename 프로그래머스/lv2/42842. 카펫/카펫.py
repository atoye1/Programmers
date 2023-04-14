def solution(brown, yellow):
    answer = []
    # 노랑 길이는 전체 길이 -2
    # 노랑 가로도 전체 너비 -2
    # 갈색의 전체 개수는 모서리 4개 + 노랑길이 * 2 + 노랑 높이 + 2 이다. 
    
    # 변수 하나를 고정시켜 놓은 상태에서 반복문을 돌린다.
    # 노랑의 가로길이를 고정시키고 돌려보자.
    for w in range(yellow, 0, -1):
        # 나누어 떨어지지 않으면 패스한다.
        if yellow % w != 0:
            continue
        h = yellow // w # 나누어 떨어졌으니 당연히 w * h == yellow는 성립한다.
        
        if brown == 4 + (w * 2) + (h * 2):
            answer = [w + 2, h + 2]
            break;
    return answer