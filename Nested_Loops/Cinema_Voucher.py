voucher = int(input())
product = input()
movie_ticket = 0
product_ticket = 0
price = 0
while product != 'End':
    text1 = product[0]
    text2 = product[1]
    if len(product) > 8:
        price = ord(text1) + ord(text2)
        if voucher >= price:
            voucher -= price
            movie_ticket += 1
        else:
            break
    if len(product) <= 8:
        price = ord(text1)
        if voucher >= price:
            voucher -= price
            product_ticket += 1
        else:
            break
    product = input()
print(movie_ticket)
print(product_ticket)
