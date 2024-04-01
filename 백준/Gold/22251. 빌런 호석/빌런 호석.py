change_counts = [[0,4,3,3,4,3,2,3,1,2],
                 [4,0,5,3,2,5,6,1,5,4],
                 [3,5,0,2,5,4,3,4,2,3],
                 [3,3,2,0,3,2,3,2,2,1],
                 [4,2,5,3,0,3,4,3,3,2],
                 [3,5,4,2,3,0,1,4,2,1],
                 [2,6,3,3,4,1,0,5,1,2],
                 [3,1,4,2,3,4,5,0,4,3],
                 [1,5,2,2,3,2,1,4,0,1],
                 [2,4,3,1,2,1,2,3,1,0]]

N,K,P,X = map(int, input().split())
x = str(X).zfill(K)
answer = 0

for i in range(1, N+1):
  count = 0
  if i == X:
    continue
  number = str(i).zfill(K)
  for i in range(K):
    count += change_counts[int(x[i])][int(number[i])]

  if count <= P:
    answer += 1

print(answer)