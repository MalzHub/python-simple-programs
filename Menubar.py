from tkinter import *

# Top-level window
window = Tk()
window.title("Menu Bar Tutorial")
window.geometry('350x200')

# Create a toplevel menu bar
menubar = Menu(window)
menubar.add_command(label="File")
menubar.add_command(label="Edit")

# Display the menu
window.config(menu=menubar)

# Run the event loop
window.mainloop()
