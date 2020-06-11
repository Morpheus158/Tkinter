from tkinter import *

def conv(gram_const=1000, pound_const=2.20462, ounce_const=35.274):
    number = float(e1_value.get())
    t1.insert(END, number * gram_const)
    t2.insert(END, number * pound_const)
    t3.insert(END, number * ounce_const)

window = Tk()

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", underline=True, command=conv)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=15)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=15)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=15)
t3.grid(row=1, column=2)

window.mainloop()