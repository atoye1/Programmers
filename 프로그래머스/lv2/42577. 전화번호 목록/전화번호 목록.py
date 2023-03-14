def solution(phone_book):
    # 입력이 백만개이므로 n^2로 풀이할 수 없다.
    # sort 로 스트링을 정렬하면 사전식으로 정렬되는 특성을 활용한다.
    # 사전식으로 정렬된다면 a를 접두어로 가지는 문자는 항상 a바로 뒤에 위치하게 된다.
    pb_sorted = sorted(phone_book) # O(nlogn)
    for i in range(len(pb_sorted) - 1): # O(n)
        # in 연산을 활용하면 접두어가 아니더라도 트루를 반환하니깐 다시
        if pb_sorted[i] == pb_sorted[i+1][0:len(pb_sorted[i])]:
            return False
    return True
