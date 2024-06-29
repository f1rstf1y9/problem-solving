from collections import deque

X = int(input())

cur_length = 64
polls = deque([64])

while True:
  if sum(polls) > X:
    half_of_poll = polls.popleft() // 2
    polls.appendleft(half_of_poll)
    if sum(polls) < X:
      polls.appendleft(half_of_poll)
  else:
    break
print(len(polls))