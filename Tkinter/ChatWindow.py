""" this program create chat window"""

from tkinter import * # import the library

root = Tk()

root.title("Chat")
root.iconbitmap("chat.ico") # add icon
root.geometry("400x500")
root.resizable(False,False) # not resizable

chat_window = Text(root,bd=1, bg="black",foreground="white",font=("David",19))
#bd=Same as borderwidth|bg=Same as background|foreground  Sam as Color text
chat_window.place(x=6,y=6, height=385, width=370)

def clicked():
    text = message_window.get("1.0",END)
    message_window.delete("1.0", END)
#The first part, "1.0" means that the input should be read from line one to the END
    chat_window.insert(END, text)

button = Button(root,command=clicked,text="Send", width="12", height="5", bg="blue",font=("David",12),foreground="white", activebackground="#0080ff" )
button.place(x=6,y=400, height=88)

message_window = Text(root, bg="black", width="30",height="4", font=("David",10), foreground= "white")
message_window.place(x=128,y=400, height=88, width=260)

scrollbar = Scrollbar(root, command=chat_window.yview)
scrollbar.place(x=375, y=5, height=385)


root.mainloop() #run the tkinter