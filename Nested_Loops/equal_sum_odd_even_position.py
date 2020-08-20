first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0
    counter = 1
    number2 = number
    while number2 > 0:
        last = number2 % 10
        if counter % 2 == 0:
            even_sum += last
        else:
            odd_sum += last
        number2 = number2 // 10
        counter += 1
    if even_sum == odd_sum:
        print(number, end=' ')
