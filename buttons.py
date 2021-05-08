from tkinter import *

root = Tk()

"""
We can use some basic parameters: 
padx = some int : change x axis width
pady = some int:  change y axis width
state = DISABLED : to make button to be unclickable
fg: change the text inside the button
bg: change background color of the button
border: border thickness of the button
command: to add functionality to the button by defining a function
"""

def myClick():
    label = Label(root, text="yoink! you clicked the button")
    label.pack()

button1 = Button(root, text="ClicK", padx=10, pady=10, command=myClick,bg='cyan', fg='black', border=10)
#button2 = Button(root, text="Don't ClicK", padx=5, pady=5)

button1.pack()
#button2.pack()

root.mainloop()

