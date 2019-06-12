from tkinter import *

root = Tk()
root.title("Frame Layout")

#creating 2 frames TOP and BOTTOM
top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side = "bottom")

#now, create some widgets in the top frame and bottom frame

btn1 = Button(top_frame, text="Button1", fg="red")   
btn1.pack()

btn2 = Button(top_frame, text="Button2", fg="green")
btn2.pack()

btn3= Button(bottom_frame, text="Button3", fg="purple")
btn3.pack(side = "left")

btn4 = Button(bottom_frame, text="Button4", fg="orange")
btn4.pack(side = "left")

#Creating 3 simple Labels containing any text

#Sufficient Width
label_one = Label(root, text=" Suf. Width", fg="white",bg="purple")
label_one.pack()

#Width of X
label_two = Label(root,text="Taking all available X Width", fg="white", bg="green")
label_two.pack(fill="x")

#Height of Y
label_three = Label(root,text="Taking all Avail Y Height", fg="white", bg="black")
label_three.pack(side="left",fill="y")





root.mainloop()