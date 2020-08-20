destination = input()

#my_money = 0

while destination != 'End':
    bidget = float(input())
    my_money = 0
   # dest = input()
    while bidget > my_money:
        money = float(input())
        my_money += money
        if my_money >= bidget:
            print(f'Going to {destination}!')
    destination = input()