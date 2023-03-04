def solution(phone_book):
    # sort 로 스트링을 정렬하면 사전식으로 정렬되는 특성을 활용한다.
    pb_sorted = sorted(phone_book)
    for i in range(len(pb_sorted) - 1):
        # in 연산을 활용하면 접두어가 아니더라도 트루를 반환하니깐 다시
        if pb_sorted[i] in pb_sorted[i + 1]:
            if pb_sorted[i] == pb_sorted[i+1][0:len(pb_sorted[i])]:
                return False
    return True
