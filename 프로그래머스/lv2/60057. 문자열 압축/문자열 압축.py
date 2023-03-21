def solution(s):
    # 입력 크기가 1000개이므로 2차시간으로 풀이 가능하다.
    
    answer = len(s)
    # 문자열을 줄이는 것은 결국 짝을 찾는 거니깐. 짝이 되려면 문자열의 길이 // 2 까지만 가능하다.
    # 예를들어 크기가 10인 문자열의 최대 검색은 5까지만 검색하면 된다.
    max_pair = len(s) // 2
    # 1부터 max_pair까지 완전탐색해서 최솟값을 리턴하면 된다.
    
    for pair_size in range(1, max_pair + 1):
        # 처음부터 pair_size만큼 잘라서 스택에 넣는다.
        # 만약 스택의 마지막 원소와 동일한 값이 나오면 스택을 pop하고, 숫자가 반영된 값을 다시 스택에 넣으면 된다.
        # 만약 남은 문자열길이가 pair_size보다 작으면 그냥 더해주면 된다.
        stack = []
        for i in range(0,len(s) - pair_size + 1, pair_size):
            now = s[i:i + pair_size]
            
            if not stack: #스택이 비어있으면 무조건 푸쉬해주면 된다.
                stack.append(now)
            else:
                before = stack.pop()
                # 이전에 있는 단어가 지금 단어랑 동일한 경우
                if now == before:
                    if stack and type(stack[-1]) == int:
                    # 만약 앞의 요소가 숫자면 숫자를 빼내고 증가된 숫자를 집어넣는다.
                        count = stack.pop()
                        count = count + 1
                        stack.append(count)
                        # 당연히 문자열도 고대로 집어 넣어야 한다.
                        stack.append(now)
                    else:
                    # 만약 앞의 요소가 문자면, 그대로 놔두고 2를 집어넣는다.
                        stack.append(2)
                        stack.append(now)
                # 이전의 단어가 지금 단어와 다른 경우 지금단어를 그대로 스택에 넣는다.
                else:
                    stack.append(before)
                    stack.append(now)
        # int는 join 메서드를 활용할 수 없으니까 str로 변환해준다.
        # 🤔 근데 map에 O(n) 시간이 걸리니깐 위의 반복문 안에서 처리하는게 더 효율적일까? 
        # 그러면 두자리 숫자는 어떡하지?
        stack = list(map(str, stack))
        # 현재 처리된 문자열의 총 길이와 페어링 되지 않은 문자열의 길이를 더해줘야 된다. 나머지 연산자를 활용한다.
        result = len(''.join(stack)) + len(s) % pair_size
        answer = min(answer, result)

    return answer