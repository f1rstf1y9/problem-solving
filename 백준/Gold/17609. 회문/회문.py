import sys
input = sys.stdin.readline

def is_palindrome(str, is_pseudo):
    p1, p2 = 0, len(str)-1
    while p1 < p2:
        if str[p1] == str[p2]:
            p1 += 1
            p2 -= 1
        else:
            if is_pseudo: return 2
            return 2 if is_palindrome(str[p1:p2], True) and is_palindrome(str[p1+1:p2+1], True) else 1
    return 0

for _ in range(int(input())):
    print(is_palindrome(input().strip(), False))