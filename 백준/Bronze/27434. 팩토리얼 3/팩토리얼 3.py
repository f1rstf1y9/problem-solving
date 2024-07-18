import sys
sys.setrecursionlimit(10**6)

def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
n = int(input())

print(fact(n))