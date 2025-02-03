def solution(key, lock):
    N = len(lock)
    M = len(key)
    
    def rotate_key(key):
        return [[key[M-j-1][i] for j in range(M)] for i in range(M)]
    
    def is_valid_key(key, x_offset, y_offset):
        extended_lock = [[0] * (N+2*M) for _ in range(N+2*M)]
        
        for i in range(N):
            for j in range(N):
                extended_lock[i+M][j+M] = lock[i][j]
        
        for i in range(M):
            for j in range(M):
                if 0 <= x_offset+i < N+2* M and 0 <= y_offset+j < N+2*M:
                    extended_lock[x_offset+i][y_offset+j] += key[i][j]
        for i in range(N):
            for j in range(N):
                if extended_lock[i+M][j+M] != 1:
                    return False
        return True
    
    
    for _ in range(4):
        key = rotate_key(key)
        for x in range(1-M, N+M):
            for y in range(1-M, N+M):
                if is_valid_key(key, x, y):
                    return True
    
    return False