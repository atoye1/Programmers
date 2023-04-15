s, n = input().split()
s = int(s)
space = ' '
bar = '-'
pipe = '|'
# n에 있는 숫자를 출력해야된다.
# 모든 숫자는 s + 2의 가로와 2s + 3의 세로로 이루어진다.
# 첫번째 줄 출력하기
# 두 번째 줄 출력하기
# 줄별로 순회한다.
for line in range(2 * s + 3):
    builder = ''
    if line == 0:
        # 가로 첫째 라인.
        for num in list(n):
            builder += space
            if num in ['1', '4']:
                builder += space * s
            else:
                builder += bar * s
            builder += space
            builder += space
    elif line == s + 1:
        for num in list(n):
            builder += space
            if num in ['1', '7', '0']:
                builder += space * s
            else:
                builder += bar * s
            builder += space
            builder += space
    elif line == 2 * s + 2:
        for num in list(n):
            builder += space
            if num in ['1', '4', '7']:
                builder += space * s
            else:
                builder += bar * s
            builder += space
            builder += space
    else:
        # 세로 줄 출력하는 부분
        if line < s + 1:  # 세로 윗부분
            for num in list(n):
                if num in ['1', '2', '3', '7']:
                    builder += space + space * s + pipe
                elif num in ['5', '6']:
                    builder += pipe + space * s + space
                else:  # 양쪽 다
                    builder += pipe + space * s + pipe
                builder += space
        else:  # 세로 아래부분
            for num in list(n):
                if num in ['1', '3', '4', '5', '7', '9']:
                    builder += space + space * s + pipe
                elif num in ['2']:
                    builder += pipe + space * s + space
                else:  # 양쪽 다
                    builder += pipe + space * s + pipe
                builder += space
    print(builder)
