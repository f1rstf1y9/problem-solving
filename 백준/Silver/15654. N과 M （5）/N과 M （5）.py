N, M = map(int, input().split())
numbers = list(sorted(map(int, input().split())))

visited = [0]*N
def bt(seq, seq_len):
    if seq_len == M:
        print(seq.strip())
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            bt(seq + f" {numbers[i]}", seq_len + 1)
            visited[i] = 0

bt('', 0)