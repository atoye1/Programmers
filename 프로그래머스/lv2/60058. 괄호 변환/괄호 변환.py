def solution(p):
    # 주어진 알고리즘을 수행하는 구현문제
    # 균형잡힌 괄호 문자열을 올바른 괄호 문자열로 변경하는 문제
    # p를 u와 v로 분리한다.
    # u와 v는 각각 어떻게 분리해야할까?
    # 보통 스택을 사용하던데, 스택에 최초의 문자열을 넣고, 스택이 빈 경우에는 균형잡힌 괄호 문자열이 된다.
    # split_string 함수로 두 문자열을 분리하는 로직은 완성했다.
    answer = correct(p)
    return answer

def correct(s):
    # 빈 문자인 경우 빈 문자열을 반환
    if len(s) == 0:
        return ''
    # 문자열 s를 두 균형잡힌 괄호 문자열로 분리한다.
    u, v = split_string(s)
    if is_valid(u):
        return u + correct(v)
    else: # 올바른 문자열이 아니므로 문제에서 주어진 로직을 실행해야 한다.
        # 1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        # 2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 붙입니다.
        # 3. ')'를 다시 붙입니다.
        result = '(' + correct(v) + ')'
        n_u = list(u)
        n_u = n_u[1:]
        n_u.pop()
        for elem in n_u:
            if elem == ')':
                result += '('
            elif elem == '(':
                result += ')'
            else:
                assert False
        
        return result
    
def is_valid(s):
    # is_valid 안에 들어오는 문자열은 항상 균형잡힌 괄호 문자열임.
    # 따라서 투포인터로 비교해나가면 올바른 괄호문자열인지 알 수 있다.
    # ⚠️ 여기서 잘못 생각했다. 투포인터로 비교하면 안된다.
    # 올바른 괄호문자열을 어떻게 판별해야하는지 생각해야한다.
    # 올바른 괄호문자열은 스택이 비었을때 ')'가 등장하면 안된다.
    # 항상 스택에 뭐가 있을 때 ')'가 나와야 한다.
    if len(s) == 0:
        return True
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
            continue
        if not stack and char == ')':
            return False
        if stack and char == ')':
            stack.pop()
        
    return True
        
    
def split_string(s):
    if len(s) == 0:
        return '', ''
    stack = [s[0]]
    idx = 1
    while stack:
        curr = stack.pop()
        if curr == s[idx]:
            stack.append(curr)
            stack.append(s[idx])
        idx += 1
    return s[:idx], s[idx:]