from tkinter import *


tk = Tk()
tk.title("Calculator")

name = Label(tk,text = "Name").grid(row = 0, column = 0)  
enter_name = Entry(tk).grid(row = 0, column = 1)

password = Label(tk,text = "Password").grid(row = 1, column = 0)  
enter_pass = Entry(tk).grid(row = 1, column = 1)

submit = Button(tk, text = "Submit").grid(row = 4, column = 0)  

tk.mainloop()  