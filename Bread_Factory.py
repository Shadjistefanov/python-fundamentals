text = input().split('|')
energy = 100
coins = 100
is_closed = False
for i in text:
    split = i.split('-')
    name = split[0]
    price = int(split[1])
    if name == 'rest':
        temp = 0
        if energy + price <= 100:
            energy += price
            temp = price
        else:
            temp = 100 - energy
            energy = 100
        print(f'You gained {temp} energy.')
        print(f'Current energy: {energy}.')
    elif name == 'order':
        if energy - 30 >= 0:
            coins += price
            energy -= 30
            print(f'You earned {price} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins - price > 0:
            coins -= price
            print(f'You bought {name}.')
        else:
            print(f'Closed! Cannot afford {name}.')
            is_closed = True
            break
if not is_closed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')

