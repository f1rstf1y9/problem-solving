from collections import Counter

def solution(a):
    if len(a) == 1:
        return 0
    counts = Counter(a)
    max_length = 0
    
    for num, freq in counts.items():
        if freq * 2 <= max_length:
            continue
        
        length = 0
        i = 0
        while i < len(a)-1:
            if (a[i] == num or a[i+1] == num) and a[i] != a[i+1]:
                length += 2
                i += 2
            else:
                i += 1
        max_length = max(max_length, length)
    
    return max_length