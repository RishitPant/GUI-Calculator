from tkinter import *

root = Tk()

#Creating button widget
label1 = Label(root, text="Hello wORLD")
#TO get text On to the screen
label1.pack() #can use this pack method
label1.grid(row=1, column = 0) # use grid to adjust your text where you want it to be
root.mainloop()
