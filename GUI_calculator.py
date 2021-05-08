from tkinter import *
import tkinter as tk

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=3, bg="#FFE8E5", fg="#330000")
e.grid(row=0, column=0, padx = 10, pady = 10, columnspan=3)


button = tk.Button(None, text='Button', font='sans 16 bold')

label = Label(root, text='')



def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    s_num = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, int(f_num + int(s_num)))

    if math == "subtraction":
        e.insert(0, int(f_num - int(s_num)))

    if math == "multiplication":
        e.insert(0, int(f_num * int(s_num)))

    if math == "division":
        e.insert(0, float(f_num / int(s_num)))


button_1 = Button(root, text="1",  padx=30, pady=20, borderwidth=4, bg="#FFEE93", font=button,fg='black', command=lambda: button_add(1))
button_2 = Button(root, text="2",  padx=30, pady=20, borderwidth=4, bg="#FFEE93", font=button, fg='black', command=lambda: button_add(2))
button_3 = Button(root, text="3",  padx=30, pady=20, borderwidth=4, bg="#FFEE93", fg='black', font=button, command=lambda: button_add(3))
button_4 = Button(root, text="4",  padx=30, pady=20, borderwidth=4, bg="#FFEE93", font=button, fg='black', command=lambda: button_add(4))
button_5 = Button(root, text="5",  padx=30, pady=20, font=button, bg="#FFEE93", borderwidth=4, fg='black', command=lambda: button_add(5))
button_6 = Button(root, text="6",  padx=30, pady=20, font=button, bg="#FFEE93", borderwidth=4, fg='black', command=lambda: button_add(6))
button_7 = Button(root, text="7",  padx=30, pady=20, font=button, bg="#FFEE93", borderwidth=4, fg='black', command=lambda: button_add(7))
button_8 = Button(root, text="8",  padx=30, pady=20, borderwidth=4, bg="#FFEE93", fg='black', font=button, command=lambda: button_add(8))
button_9 = Button(root, text="9",  padx=30, pady=20, borderwidth=4, bg="#FFEE93", font=button, fg='black', command=lambda: button_add(9))
button_0 = Button(root, text="0",  padx=30, pady=20, font=button, bg="#FFEE93", borderwidth=4, fg='black', command=lambda: button_add(0))
button_ad = Button(root, text="+",  padx=20, pady=20, bg="#B1F2EC", font=button, borderwidth=4, fg='black', command=button_plus)
button_subtract = Button(root, text="-",  padx=21, pady=20, bg="#B1F2EC", font=button, borderwidth=4, fg='black', command=button_sub)
button_multiply = Button(root, text="x",  padx=20, pady=20, bg="#B1F2EC", font=button, borderwidth=4, fg='black', command=button_mul)
button_divide = Button(root, text="/",  padx=21, pady=20, bg="#B1F2EC", font=button, borderwidth=4, fg='black', command=button_div)
button_clear = Button(root, text="Clear",  padx=22, pady=6, font=button, bg='#FF8888', borderwidth=4, fg='black', command=button_clear)
button_equal = Button(root, text="=",  padx=31, pady=6, font=button, bg='#88FF88', borderwidth=4, fg='black', command=button_equal)



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

button_clear.place(x=0, y=55)
button_equal.place(x=232, y=55)

label.grid(row=2, column=4, pady=2)
button_ad.grid(row=2, column=5)
button_subtract.grid(row=3, column=5)
button_multiply.grid(row=4, column=5)
button_divide.grid(row=5, column=5)


label.grid(row=4, column=0, pady=20)
label.grid(row=4, column=2, pady=20)
label.grid(row=1, column=0, pady=20)
#label.grid(row=1, column=2, pady=20)


root.mainloop()
