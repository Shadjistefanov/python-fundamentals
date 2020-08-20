broqt_etaji = int(input())
broq_stai = int(input())

for etaj in range(broqt_etaji, 0, -1):
    for staq in range(0, broq_stai, 1):
        if etaj == broqt_etaji:
            print(f'L{etaj}{staq}', end=' ')
        elif etaj % 2 == 0:
            print(f'O{etaj}{staq}', end=' ')
        elif etaj % 2 == 1:
            print(f'A{etaj}{staq}', end=' ')
    print()
