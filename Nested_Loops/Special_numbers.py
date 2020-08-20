n = int(input())

for first in range(1, 10):
    for second in range(1, 10):
        for three in range(1, 10):
            for four in range(1, 10):
                if n % first == 0 and n % second == 0 and n % three == 0 and n % four == 0:
                    print(f'{first}{second}{three}{four}', end=' ')