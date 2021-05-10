from tkinter import *
from math import *


root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=3, bg="#F2F7EE")
e.grid(row=0, column=0, padx = 10, pady = 10, columnspan=5)

button = Button(root, text='Button', font='sans 16 bold')
label = Label(root, text='')


def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def CE():
    e.delete(len(str(e.get()))-1)


def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def square():
    global math
    global f_num
    first_number = e.get()
    f_num = float(first_number)
    math = "square"
    current = e.get()
    e.delete(0, END)
    e.insert(0, (int(current) ^ int(first_number)))


def square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square_root"
    f_num = float(first_number)
    e.delete(0, END)


def dot(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def pi():
    e.insert(0, float(3.14))


def button_equal():
    global f_num
    global math
    s_num = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, float(float(f_num) + float(s_num)))

    if math == "subtraction":
        e.insert(0, float(float(f_num) - float(s_num)))

    if math == "multiplication":
        e.insert(0, float(float(f_num) * float(s_num)))

    if math == "division":
        e.insert(0, float(float(f_num) / float(s_num)))

    if math == "square":
        e.insert(0, float(f_num ** int(2)))

    if math == "square_root":
        e.insert(0, float(sqrt(f_num)))


button_1 = Button(root, text="1",  padx=30, pady=20, borderwidth=4, bg="#FEF7E7", font=button,fg='black', command=lambda: button_add(1))
button_2 = Button(root, text="2",  padx=30, pady=20, borderwidth=4, bg="#FEF7E7", font=button, fg='black', command=lambda: button_add(2))
button_3 = Button(root, text="3",  padx=30, pady=20, borderwidth=4, bg="#FEF7E7", fg='black', font=button, command=lambda: button_add(3))
button_4 = Button(root, text="4",  padx=30, pady=20, borderwidth=4, bg="#FEF7E7", font=button, fg='black', command=lambda: button_add(4))
button_5 = Button(root, text="5",  padx=30, pady=20, font=button, bg="#FEF7E7", borderwidth=4, fg='black', command=lambda: button_add(5))
button_6 = Button(root, text="6",  padx=30, pady=20, font=button, bg="#FEF7E7", borderwidth=4, fg='black', command=lambda: button_add(6))
button_7 = Button(root, text="7",  padx=30, pady=20, font=button, bg="#FEF7E7", borderwidth=4, fg='black', command=lambda: button_add(7))
button_8 = Button(root, text="8",  padx=30, pady=20, borderwidth=4, bg="#FEF7E7", fg='black', font=button, command=lambda: button_add(8))
button_9 = Button(root, text="9",  padx=30, pady=20, borderwidth=4, bg="#FEF7E7", font=button, fg='black', command=lambda: button_add(9))
button_0 = Button(root, text="0",  padx=30, pady=20, font=button, bg="#FEF7E7", borderwidth=4, fg='black', command=lambda: button_add(0))
button_ad = Button(root, text="+",  padx= 24, pady=20, bg="#FFD8B3", font=button, borderwidth=4, fg='black', command=button_plus)
button_subtract = Button(root, text="-",  padx=24, pady=20, bg="#FFD8B3", font=button, borderwidth=4, fg='black', command=button_sub)
button_multiply = Button(root, text="x",  padx=24, pady=20, bg="#FFD8B3", font=button, borderwidth=4, fg='black', command=button_mul)
button_divide = Button(root, text="/",  padx=25, pady=20, bg="#FFD8B3", font=button, borderwidth=4, fg='black', command=button_div)
button_clear = Button(root, text="C",  padx=29, pady=10, font=button, bg='#FF8888', borderwidth=4, fg='black', command=button_clear)
button_equal = Button(root, text="=",  padx=30, pady=20, font=button, bg='#88FF88', borderwidth=4, fg='black', command=button_equal)
btn_decimal=Button(root,text=u'\u002E',padx=27,pady=22, borderwidth=4, bg="#FFD8B3", command=lambda:dot("."))
button_pi = Button(root, text='π', padx=21, pady=20, bg="#FFD8B3", font=button, borderwidth=4, command=pi)
button_CE = Button(root, text="CE", padx=22, pady=20, font=button, bg="#99B2FF", borderwidth=4, command=CE)
button_square = Button(root, text='x2', padx=19, pady=19, font=button, bg="#FFD8B3", borderwidth=4, command=square)
button_squareroot = Button(root, text='√', padx = 22, pady=20, font=button, bg="#FFD8B3", borderwidth=4, command=square_root)


button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_0.grid(row=5, column=1)
button_pi.grid(row=4, column=4)
button_clear.grid(row=1, column=0)
button_CE.grid(row=5, column=0)
button_equal.grid(row=5, column=2)
btn_decimal.grid(row=5, column=3)
button_squareroot.grid(row=3, column=4)
button_ad.grid(row=2, column=3)
button_subtract.grid(row=2, column=4)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_square.grid(row=5, column=4)


root.mainloop()
