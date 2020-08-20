movie = input()
total_ticket = 0
student_ticket = 0
standard_ticket = 0
kids_ticket = 0
while movie != 'Finish':
    free_space = int(input())
    ticket_type = input()
    count_ticket = 0
    while ticket_type != 'End':
        count_ticket += 1
        total_ticket += 1
        if ticket_type == 'student':
            student_ticket += 1
        elif ticket_type == 'standard':
            standard_ticket += 1
        elif ticket_type == 'kid':
            kids_ticket += 1
        if count_ticket >= free_space:
            break
        ticket_type = input()
    percent = count_ticket / free_space * 100
    print(f'{movie} - {percent:.2f}% full.')
    movie = input()
if movie == 'Finish':
    print(f'Total tickets: {total_ticket}')
    student_percent = student_ticket / total_ticket * 100
    print(f'{student_percent:.2f}% student tickets.')
    standard_percent = standard_ticket / total_ticket * 100
    print(f'{standard_percent:.2f}% standard tickets.')
    kids_percent = kids_ticket / total_ticket * 100
    print(f'{kids_percent:.2f}% kids tickets.')

