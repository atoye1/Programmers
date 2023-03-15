from collections import Counter
def solution(id_list, report, k):
    answer = []
    # 동일한 신고는 하나로 처리해준다
    report = set(report)
    # 카운터를 만들어서 각각 신고가 얼마나 들어왔는지 파악한다.
    report_counter=dict()
    reporter_counter=dict()
    # 리포트는 200,000개 이므로 선형로그시간 이하로 풀어야 한다. 여기서는 상수시간으로 처리해본다.
    for elem in report:
        reporter, reported = elem.split()
        # 딕셔너리의 키가 없는 경우 0을 초기값으로 설정한다.
        # 신고받은 카운트를 계수해준다.
        report_counter.setdefault(reported, 0)
        report_counter[reported] += 1
        # 딕셔너리의 키가 없는 경우 0을 초기값으로 설정한다.
        # 내가 신고한 사람의 리스트를 딕셔너리의 밸류로 저장한다.
        reporter_counter.setdefault(reporter, [])
        reporter_counter[reporter].append(reported)
    for user in id_list:
        result = 0
        # 내가 신고한 목록을 추출한다.
        if not reporter_counter.get(user):
            answer.append(result)
            continue
        for i in reporter_counter[user]:
            if report_counter.get(i) >= k:
                result += 1
        # 그 목록중의 사람의 카운터를 체크하는데, k이상이면 내 결과를 1 증가시킨다.
        answer.append(result)
    
    return answer