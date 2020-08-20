n = int(input())
num = 1
bigger_than_n = False

for row in range(1, n + 1):
    for cols in range(1, row + 1):

        if num > n:
            bigger_than_n = True
            break
        print(num, end=' ')
        num += 1
    if bigger_than_n:
        break
    print()