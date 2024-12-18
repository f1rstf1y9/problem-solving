import sys
input = sys.stdin.readline

N = int(input())
expected_grades = sorted([int(input()) for _ in range(N)])

total_complaint = sum([abs(i - expected_grades[i-1]) for i in range(1, N+1)])
print(total_complaint)