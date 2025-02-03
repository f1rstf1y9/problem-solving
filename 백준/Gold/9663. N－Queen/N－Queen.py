N = int(input())
answer = 0

col = [0]*N
up_diag = [0]*(2*N-1)
down_diag = [0]*(2*N-1)

def check_col_diag_info(x, y, bool):
    col[y] = up_diag[x+y] = down_diag[x-y+N-1] = bool

def backtracking(n):
    global answer
    if n == N:
        answer += 1
        return
    for j in range(N):
        if not (col[j] or up_diag[n+j] or down_diag[n-j+N-1]):
            check_col_diag_info(n, j, 1)
            backtracking(n+1)
            check_col_diag_info(n, j, 0)

backtracking(0)
print(answer)