K = int(input())

length = 1
count = 0

while count + (2**length) < K:
    count += (2**length)
    length += 1

remaining = K - count

answer = ['4'] * length

for i in range(length):
    if remaining > 2 ** (length-i-1):
        answer[i] = '7'
        remaining -= 2 ** (length-i-1)

print(*answer, sep="")