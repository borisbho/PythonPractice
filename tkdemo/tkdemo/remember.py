from tkinter import Tk, Label, Frame, Button, Entry, Canvas, PhotoImage
import random
root = Tk()
root.title('Remember The GUI Year')

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

def doEntry():
    score = int(label_counter['text'])
    year_input = int(entry_name.get())
    event_year = list_of_questions[question_number-1][1]
    if year_input == event_year:
        score += 10
        label_message.config(text= '10 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year))
    elif abs(year_input-event_year) <= 5:
        score += 5
        label_message.config(text='5 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year))
    elif abs(year_input-event_year) > 5 and abs(year_input-event_year) <= 10:
        score += 1
        label_message.config(text='2 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year))
    else:
        label_message.config(text='0 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year))
    label_title.config(text = "In What Year was"  + " " + list_of_questions[question_number][0])


label_question_number = Label(
    text = '1',
    fg = '#000',
    font = "Arial 20 bold italic"
)
question_number = int(label_question_number['text'])

label_question_number.grid(column=0,row=0)   

label_title = Label(
    text ="In What Year was"  + " " + list_of_questions[question_number][0],
    fg = "#000",
    font = "Arial 20 bold italic"
)
label_title.grid(column=1, row=0)

label_counter = Label( 
    text='0',
    bg='dark blue',
    fg='#ff0',
    width=4,
    font = 'Arial 14 bold italic'
)

label_counter.grid(column=2, row =3)

btn_submit = Button(
    text='SUBMIT',
    bg='turquoise',
    fg='black',
    width=9,
    command = doEntry
 )
btn_submit.grid(column=0,row=4)

frame_entry = Frame(root)
frame_entry.grid(column=0, row=3)



entry_name = Entry(frame_entry)
entry_name.pack(side='top')

label_message = Label(
    text ="",
    fg = "#000",
    font = "Arial 20 bold italic"
)
label_message.grid(column=1, row=2)
 
                
                    
root.mainloop()

















#question_number = int(label_question_number['text'])
 

# def doEntry():
#     score = int(label_counter['text'])
#     year_input = int(entry_name.get())
#     event_year = list_of_questions[question_number-1][1]
#     if year_input == event_year:
#         score += 10
#         label_message.config(text= '10 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year))
#     elif abs(year_input-event_year) <= 5:
#         score += 5
#         label_message.config(text='5 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year))
#     elif abs(year_input-event_year) > 5 and abs(year_input-event_year) <= 10:
#         score += 1
#         label_message.config(text='2 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year))
#     else:
#         label_message.config(text='0 Points | Score: ' + str(score) +  '| Correct Answer: ' + str(event_year))
                
                                         
    # i = 9
    # final_score = 0
    # question_number = 1

    # while i is not -1:
    #     try:        
    #         random_int = 0
    #         year_input = int(entry_name.get())
    #         event_year = list_of_questions[random_int][1]
    #         label_title.config(text="In What Year was "  + " " + list_of_questions[random_int][0])
            # if year_input == event_year:
            #     final_score += 10
            #     label_message.config(text= '10 Points | Score: ' + str(final_score) +  '| Correct Answer: ' + str(event_year))
                
            # elif abs(year_input-event_year) <= 5:
            #     final_score += 5
            #     label_message.config(text='5 Points | Score: ' + str(final_score) +  '| Correct Answer: ' + str(event_year))
                
    #         elif abs(year_input-event_year) > 5 and abs(year_input-event_year) <= 10:
    #             final_score += 1
    #             label_message.config(text='2 Points | Score: ' + str(final_score) +  '| Correct Answer: ' + str(event_year))
                                
    #         elif abs(year_input-event_year) > 10 and abs(year_input-event_year) <= 20:
    #             final_score += 1
    #             label_message.config(text='1 Points | Score: ' + str(final_score) +  '| Correct Answer: ' + str(event_year))
                
            # else:
            #     label_message.config(text='0 Points | Score: ' + str(final_score) +  '| Correct Answer: ' + str(event_year))
                
            # del list_of_questions[random_int]
            # i -= 1
            # question_number += 1
            # random_int += 1
            # entry_name.delete(0,'end')
    #     except ValueError:
    #          break

    # if final_score == 100:
    #     label_message.config(text='Total Score: ' + str(final_score) + ', You did really good!\n')
    # elif final_score < 100 and final_score >= 70:
    #     label_message.config(text='Total Score: ' + str(final_score) + ', You did alright!')
        
    # else:
    #     label_message.config(text='Total Score: ' + str(final_score) + ', Youre Trash!')