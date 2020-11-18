
from tkinter import * # import tkinter
from tkinter.ttk import * # for more methods like Combobox

window = Tk() # open window arguments as tkinter objects in

# configuration of window
window.title("this is my fisrt windows") # titlw of the windows
window.iconbitmap("google.ico") # add icon on window
window.geometry("500x500") # size of window X x Y
window.resizable(False,False) # lock the size of window X Y

# deals with window
text_label = Label(window, text="Hello to you") # Label is text on window
text_label.grid(column =0 , row= 0)
text_label = Label(window, text="whats is your name",font =("David", 15)) # Label is text on window
text_label.grid(column =0 , row= 1)

def clicked(): # function that show text on label
    result_text.configure(text = entry_text.get())
    print(combo_box.get())


button_click = Button(window, text="Click me!", command = clicked)
button_click.grid(column =0, row=2)

entry_text = Entry(window,width=20) # put data
entry_text.grid(column =1, row =1)

result_text = Label(window) # create empty label
result_text.grid(column =0 , row =3)

combo_box = Combobox(window, values = (1,2,3,4))
combo_box.grid(column =2, row = 2)
combo_box.current(2)
print(combo_box.get())

#window.mainloop() # run the program
window.mainloop()
