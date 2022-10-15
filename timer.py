#Importing Libraries
from tkinter import *
from tkinter.ttk import *
from time import strftime

#Initializing root
root = Tk()
root.title("Abrar Hussain @ TIME")

#defining time function
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

#Creating GUI Environment
label = Label(root, font=("Times New Roman",80), background="#0000A6", foreground="#FF8000")
label.pack(anchor="center")

time()

mainloop()