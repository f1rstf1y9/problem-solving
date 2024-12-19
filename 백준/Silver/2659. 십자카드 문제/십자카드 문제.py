def get_clock_number(n1, n2, n3, n4):
    n1, n2, n3, n4 = str(n1), str(n2), str(n3), str(n4)
    return min(int(n1+n2+n3+n4), int(n2+n3+n4+n1), int(n3+n4+n1+n2), int(n4+n1+n2+n3))
clock_numbers = set()
for n1 in range(1,10):
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            for n4 in range(1, 10):
                clock_numbers.add(get_clock_number(n1, n2, n3, n4))

n1, n2, n3, n4 = map(int, input().split())
cur_clock_number = get_clock_number(n1, n2, n3, n4)

print(sorted(list(clock_numbers)).index(cur_clock_number)+1)