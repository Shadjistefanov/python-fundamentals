team_count = int(input())
counter = 0
grades_sum = 0
while True:
    presentation_name = input()
    if presentation_name == 'Finish':
        break
    presentation = presentation_name
    current_grades_sum = 0
    for i in range(team_count):
        grade = float(input())
        grades_sum += grade
        counter += 1
        current_grades_sum += grade
    average_grade = current_grades_sum / team_count
    print(f'{presentation} - {average_grade:.2f}.')
average = grades_sum / counter
print(f"Student's final assessment is {average:.2f}.")
