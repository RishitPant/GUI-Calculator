from tkinter import *

root = Tk()

e = Entry(root, width=50)

'''
We can use basic parameters:
width= some int: To change the width of the input box
fg and bg to change the text color and the background color of the input area
borderwidth = some int : to change the border of the input area/box
'''

e.pack()
e.insert(0, " Whatever Text you want in here") # This will put default text into the input area whatever you will type in the insert thing.


'''
In this below " myClick function " we used " e.get() " which takes the input from the input area
whatever is typed in there. and we can add into label and trigger the function when the button
Is clicked
'''

def myClick():
    variable = "Yo " + e.get()
    label = Label(root, text = variable)
    label.pack()

button1 = Button(root, text="ClicK", padx=10, pady=10, command=myClick, border=3)
button1.pack()

root.mainloop()