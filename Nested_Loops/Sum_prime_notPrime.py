
prime_sum = 0
not_prime_sum = 0

while True:
    command = input()
    if command == 'stop':
        break
    number = int(command)
    if number < 0:
        print('Number is negative.')
        continue

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += number
    else:
        not_prime_sum += number

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {not_prime_sum}')

