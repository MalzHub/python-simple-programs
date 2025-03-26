from tkinter import *

window = Tk()
window.title("Check Box Tutorial")

varReg = IntVar()
varEnqui = IntVar()

def clicked(value):
    myLabel = Label(window, text=value)
    myLabel.pack()
    print(value)

Checkbutton(window, text="Registration", variable=varReg, 
            command=lambda: clicked(varReg.get())).pack(anchor=W)

Checkbutton(window, text="Enquiry", variable=varEnqui, 
            command=lambda: clicked(varEnqui.get())).pack(anchor=W)

window.mainloop()
