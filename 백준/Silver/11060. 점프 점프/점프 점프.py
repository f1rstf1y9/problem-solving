from collections import deque

def min_jumps(N, A):
    if N == 1:
        return 0

    queue = deque([(0, 0)])
    visited = [False] * N
    visited[0] = True

    while queue:
        idx, jumps = queue.popleft()

        # A[idx]의 범위 내에서 가능한 점프를 확인
        for i in range(1, A[idx] + 1):
            next_idx = idx + i
            if next_idx >= N - 1:
                return jumps + 1
            if not visited[next_idx]:
                visited[next_idx] = True
                queue.append((next_idx, jumps + 1))

    return -1

N = int(input())
A = list(map(int, input().split()))
print(min_jumps(N,A))