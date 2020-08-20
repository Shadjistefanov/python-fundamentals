count_movie = int(input())
count_rate = 0
max_rate = -120000.0
min_rate = 120000.0
name = ''
counter = 0
name_win = ''
name_lose = ''
for i in range(count_movie):
    name = input()
    rate = float(input())
    counter += 1
    if rate > max_rate:
        max_rate = rate
        name_win = name
    if rate < min_rate:
        min_rate = rate
        name_lose = name
    count_rate += rate
#if count_movie <= counter:
print(f'{name_win} is with highest rating: {max_rate:.1f}')
print(f'{name_lose} is with lowest rating: {min_rate:.1f}')
print(f'Average rating: {count_rate / count_movie:.1f}')
