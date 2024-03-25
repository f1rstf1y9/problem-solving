N, t_score, P = map(int, input().split())
if N == 0:
  print(1)
else:
  ranking = list(map(int, input().split()))
  if len(ranking) == P and ranking[-1] >= t_score:
    print(-1)
  else:
    rank = 1
    for score in ranking:
      if score > t_score:
        rank += 1
    print(rank)