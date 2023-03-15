def solution(number, k):
    '''
        백만의 입력인 경우도 있으므로 선형시간으로 풀이해야한다.
        탐욕법이 적용되는 문제이다. 최적해를 구하는 문제
        1. 앞에서 최선의 선택을 했다면 뒤의 결과와는 독립이다.
        2. 따라서 앞에서부터 최선의 선택을 해나가고, 그것을 누적한 것이
        3. 최적해가 될 수 있다.
    '''
    stack = []
    for i, num in enumerate(number):
        # 만약 스택의 마지막 숫자가 현재 넣으려는 숫자보다 작다면
        # 그리고 제거 카운트가 남아 있어서 제거가 가능하다면
        # 숫자를 제거해줘야 한다.
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        # 추가적으로 연산을 줄이기 위해 k가 0인 경우 일괄 이어 붙인다.
        if k == 0:
            stack += number[i:]
            break
        stack.append(num)
    # 반복문이 끝났는데도 k가 남아 있는 경우 처리
    stack = stack[:-k] if k > 0 else stack
    answer = ''.join(stack)
    return answer