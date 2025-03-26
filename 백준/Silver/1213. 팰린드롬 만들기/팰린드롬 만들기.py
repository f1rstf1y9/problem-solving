import sys
name = sys.stdin.readline().strip()

alpha_count = [0]*26

for alpha in name:
    alpha_count[ord(alpha)-65] += 1

answer = ''
single_alpha = ''

for i in range(26):
    if alpha_count[i] % 2 and single_alpha:
        print("I'm Sorry Hansoo")
        break
    answer += chr(i+65)*(alpha_count[i]//2)
    single_alpha = chr(i+65) if alpha_count[i]%2 else single_alpha
else:
    answer = answer + single_alpha + ''.join(reversed(answer))
    print(answer)