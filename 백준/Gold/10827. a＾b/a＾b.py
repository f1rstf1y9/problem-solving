a, b = input().split()

int_a, float_a = a.split('.')

a = int(int_a + float_a)
b = int(b)
int_result = str(a ** b)

dot_place = len(float_a) * b

if len(int_result) <= dot_place:
    int_result = '0' * dot_place + int_result

float_result = int_result[0:-dot_place]+'.'+int_result[-dot_place:]

start_idx = 0
end_idx = len(float_result)

for i in range(len(float_result)):
    start_idx = i
    if float_result[i] == '.':
        start_idx -= 1
        break
    if float_result[i] != '0':
        break


for i in range(len(float_result)-1,-1,-1):
    if float_result[i] != '0':
        break
    end_idx = i

print(float_result[start_idx:end_idx])