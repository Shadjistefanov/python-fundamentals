name = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0
percent_movie = 0
percent_student = 0
percent_standard = 0
percent_kid = 0
while name != 'Finish':
    free_space = int(input())
    tickets = 0
    # total_tickets += 1
    for i in range(free_space):
        ticket_type = input()
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
        if ticket_type == 'End':
            break
        tickets += 1
        total_tickets += 1
    percent_movie = (tickets / free_space) * 100
    print(f'{name} - {percent_movie:.2f}% full.')
    name = input()
if name == 'Finish':
    percent_student = (student_tickets / total_tickets) * 100
    percent_standard = (standard_tickets / total_tickets) * 100
    percent_kid = (kid_tickets / total_tickets) * 100
    print(f'Total tickets: {total_tickets}')
    print(f'{percent_student:.2f}% student tickets.')
    print(f'{percent_standard:.2f}% standard tickets.')
    print(f'{percent_kid:.2f}% kids tickets.')



