S = input()
Q = int(input())

freq = [[0]*26 for _ in range(len(S)+1)]
for i in range(len(S)):
    ch = ord(S[i]) - 97
    for j in range(26):
        freq[i][j] = freq[i-1][j]
    freq[i][ch] += 1

for _ in range(Q):
    A, B, C, D = map(int, input().split())
    for i in range(26):
        X_freq = freq[B-1][i] - freq[A-2][i]
        Y_freq = freq[D-1][i] - freq[C-2][i]
        if Y_freq < X_freq:
            print("NE")
            break
    else:
        print("DA")
