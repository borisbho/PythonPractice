from tkinter import Tk, Label, Frame, Button, Entry, Canvas, PhotoImage

root = Tk()
root.title('Tkinter Demo')

counter = 0
def countUp():
    global counter
    counter +=1
    label_counter.config(text=str(counter))

def countDown():
    global counter
    counter -=1
    label_counter.config(text=str(counter))
#MESSAGE ON TOP
def doEntry():
    label_title.config(text='Hello '+entry_name.get()+'!')

label_title = Label(
    text = "Tkinter Demo",
    fg = "#007",
    font = "Arial 20 bold italic"
)
label_title.grid(column=1, row=0)

frame_counter = Frame(root)
frame_counter.grid(column=2, row=1)

label_counter = Label(frame_counter,
    text='0',
    bg='dark blue',
    fg='#ff0',
    width=4,
    font = 'Arial 14 bold italic'
)
label_counter.pack(side='top')

btn_counter_up = Button(frame_counter,
    text='Up',
    bg='turquoise',
    fg='black',
    width=9,
    command=countUp
)
btn_counter_up.pack(side='top')

btn_counter_down = Button(frame_counter,
    text='Down',
    bg='turquoise',
    fg='black',
    width=9,
    command=countDown
)
btn_counter_down.pack(side='top')

frame_entry = Frame(root)
frame_entry.grid(column=0, row=1)

Label(
    frame_entry,
    text='Name:'
).pack(side='top')

entry_name = Entry(frame_entry)
entry_name.pack(side='top')

#SUBMIT BUTTON
btn_entry = Button(frame_entry,
    text='Submit',
    width=9,
    command=doEntry
)
btn_entry.pack(side='top')

canvas = Canvas(root,
    width=200,
    height=300,
    bg='#000'
)
canvas.grid(column=1, row=1)

image_wasp = PhotoImage(file='wasp.gif')

img_y = 0

def anim_loop():
    global img_y
    canvas.delete('all')
    canvas.create_text(100,150,
        text='Howdy!',
        font='Verdana 14 bold',
        fill='#ff0'
    )
    canvas.create_image(0,img_y,anchor='nw', image=image_wasp)
    img_y += 1

    if img_y > 300:
        img_y = -120

    for i in range(0, 200, 10):
        
        canvas.create_line(200,100+i,200-i,300,fill='#0f0')

    canvas.create_rectangle(10, 50, 30, 70, fill='#f00')
    canvas.after(10, anim_loop)

anim_loop()
root.mainloop()
