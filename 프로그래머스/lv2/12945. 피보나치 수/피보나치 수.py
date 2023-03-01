def solution(n):
    if (n == 1):
        fibNum == 1
    elif (n == 0):
        fibNum = 0
    else:
        num1 = 0;
        num2 = 1;
        for i in range(2, n + 1):
            fibNum = num1 + num2;
            num1 = num2;
            num2 = fibNum;
        
    answer = fibNum % 1234567
    return answer