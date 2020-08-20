n = int(input())
l = int(input())
for first in range(1, n):
    for second in range(1, n):
        for three in range(97, 97 + l):
            for four in range(97, 97 + l):
                for five in range(2, n + 1):
                    three_chr = chr(three)
                    four_chr = chr(four)
                    if five > first and five > second:
                        print(f'{first}{second}{three_chr}{four_chr}{five}', end=' ')

