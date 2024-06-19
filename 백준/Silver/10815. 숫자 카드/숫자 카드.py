_ = int(input())
number_cards = {x: 1 for x in input().split()}
_ = int(input())
print(*[number_cards.get(x, 0) for x in input().split() ])