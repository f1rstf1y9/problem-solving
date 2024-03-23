games = {'Y': 1, 'F': 2, 'O': 3}
N, game = input().split()
N = int(N)
print(len(set([input() for i in range(N)])) // games[game])