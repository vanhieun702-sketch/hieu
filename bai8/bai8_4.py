from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('500x700+100+50')
lbl = Label(window, text="Hello", font = 'arial 15 bold')
lbl.place(x = 200 , y = 300)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked, bg = 'yellow', fg = 'blue')
btn.place(x= 250, y = 350)
window.mainloop()
