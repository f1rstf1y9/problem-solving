print("int a;")
for i in range(int(input())):
    prev_num = str(i) if i > 1 else ''
    num = str(i+1) if i else ''
    print(f"int {'*'*(i+1)}ptr{num} = &{'ptr' if i else 'a'}{prev_num};")