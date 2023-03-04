def solution(s):
    count = 0
    for char in s:
        if ord(char) >= ord('0') and ord(char) <= ord('9'):
            count += 1
            continue
        else:
        	return False
    if count == 4 or count == 6:
        return True
    return False