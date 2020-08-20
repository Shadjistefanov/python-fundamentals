first_space = int(input())
end_space = int(input())
magic_num = int(input())
combinations = 0
is_found = False
for a in range(first_space, end_space + 1):
    for b in range(first_space, end_space + 1):
        combinations +=1
        if a + b == magic_num:
            print(f'Combination N:{combinations} ({a} + {b} = {magic_num})')
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f'{combinations} combinations - neither equals {magic_num}')

