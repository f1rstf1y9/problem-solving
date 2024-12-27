N = int(input())
head, tail = input().split('*')
head_len, tail_len = len(head), len(tail)

for _ in range(N):
    file_name = input()
    if head_len+tail_len <= len(file_name) and file_name[:head_len] == head and file_name[len(file_name)-tail_len:] == tail:
        print("DA")
    else:
        print("NE")