def solution(n, lost, reserve):
    net_lost = [i for i in lost if i not in reserve]
    net_reserve = [i for i in reserve if i not in lost]
    
    net_lost.sort()
    net_reserve.sort()
    saved = 0
    p1, p2 = (0, 0)
    while p1 < len(net_lost) and p2 < len(net_reserve):
        if abs(net_lost[p1] - net_reserve[p2]) <= 1:
            p1 += 1
            p2 += 1
            saved += 1
        elif net_lost[p1] > net_reserve[p2]:
            p2 += 1
        else:
            p1 += 1
        
    return n - len(net_lost) + saved