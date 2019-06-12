import random

question_1 = ("the start of the Revolutionary War", 1775)
question_2 = ("the United States Constitution signed", 1783)
question_3 = ("President Lincoln assassinated", 1865)
question_4 = ("Theodore Roosevelt's first day in office as President of the United States", 1901)
question_5 = ("the beginning of World War II", 1939)
question_6 = ("the first personal computer introduced", 1975)
question_7 = ("the Berlin Wall taken down", 1989)
question_8 = ("the seattle seahawks superbowl champions", 2013)
question_9 = ("the social media company facebook started", 2004)
question_10 = ("the company amazon started", 1994)

list_of_questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]
random.shuffle(list_of_questions)

i = 9
final_score = 0
question_number = 1
while i is not -1:
    try:        
        random_int = 0
        year_input = int(input(f'{question_number}.) In what year was {list_of_questions[random_int][0]}:  '))
        event_year = list_of_questions[random_int][1]
        if year_input == event_year:
            final_score += 10
            print(f'\n      10 Points | Score: {final_score} | Correct Answer: {event_year}\n')
        elif abs(year_input-event_year) <= 5:
            final_score += 5
            print(f'\n      5 Points | Score: {final_score} | Correct Answer: {event_year}\n')
        elif abs(year_input-event_year) > 5 and abs(year_input-event_year) <= 10:
            final_score += 1
            print(f'\n      2 Points | Score: {final_score} | Correct Answer: {event_year}\n')                
        elif abs(year_input-event_year) > 10 and abs(year_input-event_year) <= 20:
            final_score += 1
            print(f'\n      1 Points | Score: {final_score} | Correct Answer: {event_year}\n')
        else:
            print(f'\n      0 Points | Score: {final_score} | Correct Anser: {event_year}\n')
        del list_of_questions[random_int]
        i -= 1
        question_number += 1
        random_int += 1
    except ValueError:
        break

if final_score == 100:
    print(f'\n*Total Score: {final_score}, You did really good!\n')
elif final_score < 100 and final_score >= 70:
    print(f'\n*Total Score: {final_score}, You did alright!\n')
else:
    print(f'\n*Total Score: {final_score}, Youre Trash!\n')


