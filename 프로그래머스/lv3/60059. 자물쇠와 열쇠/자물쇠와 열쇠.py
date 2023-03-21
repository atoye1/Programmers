def rotate_by_90(key):
    n = len(key)
    m = len(key[0])
    new_key = [[0] * n  for _ in range(m)]
    
    for i in range(len(key)):
        for j in range(len(key[i])):
            new_key[j][n - i - 1] = key[i][j]
            
    return new_key

def check_lock(new_lock):
    n = len(new_lock) // 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if new_lock[i][j] != 1:
                return False
    return True
            
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_by_90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check_lock(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False