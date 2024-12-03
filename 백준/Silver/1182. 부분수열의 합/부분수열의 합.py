def calc_subseq_sum(idx, cur_sum, selected_cnt): # 현재 원소 index, 현재까지의 합
    global count
    if idx == N:
        if cur_sum == S and selected_cnt:
            count += 1
        return

    calc_subseq_sum(idx+1, cur_sum + seq[idx], selected_cnt+1)
    calc_subseq_sum(idx+1, cur_sum, selected_cnt)
    

N, S = map(int, input().split())
seq = list(map(int, input().split()))
count = 0
calc_subseq_sum(0, 0, 0)

print(count)