while True:
    try:
        s, t = input().split()
        len_s, len_t = len(s), len(t)
        s_idx = 0
        for t_idx in range(len_t):
            if t[t_idx] == s[s_idx]:
                s_idx += 1
                if s_idx == len_s:
                    print("Yes")
                    break
        else:
            print("No")
    except EOFError:
        break