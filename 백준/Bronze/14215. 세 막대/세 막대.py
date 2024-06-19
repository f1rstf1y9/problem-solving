a, b, c = sorted(map(int, input().split()))
print(a + b + (c if (a+b>c) else (a + b - 1)))