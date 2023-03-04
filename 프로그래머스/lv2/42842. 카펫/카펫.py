def solution(brown, yellow):
    total = brown + yellow
    answer = [None, None];
    for width in range(total - 1, 0, -1):
        if total % width != 0:
            continue
        height = total / width
        calculated_y = (width - 2) * (height - 2)
        calculated_b = total - calculated_y
        if yellow == calculated_y and brown == calculated_b:
            answer[0] = width
            answer[1] = height
            return answer