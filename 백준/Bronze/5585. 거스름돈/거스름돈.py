money = 1000 - int(input())
answer = 0

for coin in [500,100,50,10,5,1]:
  if money == 0:
    break
  answer += money // coin
  money -= (money//coin)*coin

print(answer)