from tkinter import Tk, Label, Frame, Button, Entry, Canvas, PhotoImage
import random
 

master = Tk()
master.title('Remember The GUI Year')

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
#list_of_questions = [question_1, question_2]

list_of_questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]
random.shuffle(list_of_questions)

question_number = 0
game_score = 0

def submitAnswer():
    question_text.after(1000,lambda:question_text.config(text='nice'))
    question_year_answer = int(question_answer.get())
    event_year_answer = list_of_questions[0][1]    
    score = int(score_text['text'])
    if question_year_answer == event_year_answer:
        score += 10
        question_text.config(text='10 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year_answer))
    elif abs(question_year_answer-event_year_answer) <= 5:
        score += 5
        game_text.config(text='5 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year_answer))        
    elif abs(question_year_answer-event_year_answer) > 5 and abs(question_year_answer-event_year_answer) <= 10:
        score += 1
        game_text.config(text='1 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year_answer))
    else:
        game_text.config(text='0 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year_answer))
    score_text.config(text=str(score))
    question_answer.delete(0,'end')
    getNextQuestion()
    
def getNextQuestion():
    number_question = int(question_number_text['text'])
    if len(list_of_questions) > 1:
        list_of_questions.pop(0)
        question_text.config(text="In What Year was"  + " " + str(list_of_questions[0][0]) + " " + str(list_of_questions[0][1]))
        question_number_text.config(text=str(number_question + 1))
    else:
        final_label.config(text="Final Score: " + score_text['text'])
        question_text.config(text='Game Over!')
        score_text.grid_remove()
        question_answer.grid_remove()
        question_number_text.grid_remove()
        enter_year_text.grid_remove()
        submit_button.grid_remove()
        game_text.grid_remove()


#Text for Question Number
question_number_text = Label(text=str(question_number+1))
question_number_text.grid(row=0,column=0)

#Textbox for the Question
question_text = Label(text="In What Year was"  + " " + str(list_of_questions[0][0]) + " " + str(list_of_questions[0][1]), wraplength = 150)
question_text.grid(row=0,column=1) 

final_label = Label(master)
final_label.grid(row=4,column=1)

#User's Answer Entrybox
question_answer = Entry(width=15)
question_answer.grid(row=3, column=1) 

#Submit button to submit answer
submit_button = Button(text='Submit', width=10, command=submitAnswer)
submit_button.grid(row=4,column=1) 

#Textbox for user's score/Scoreboard
score_text = Label(text=str(game_score), bg='dark blue', fg='#fff', width=4)
score_text.grid(column=3,row=3)

#Game Message to determine if answer is right or wrong
game_text = Label(text="")
game_text.grid(row=6,column=1)


#Enter Year Text
enter_year_text = Label(text='Enter Year')
enter_year_text.grid(row=3, column=0) 

#spacing 
Label(master).grid(row=5,column=1)
Label(master).grid(row=1,column=0)

master.mainloop() 