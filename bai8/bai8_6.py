from tkinter import *
def NewFile():
    print("New File!")

def OpenFlie():
    print("Open File")    
def About():
    print("This is a simple example of a menu")
    
def Instext():
    print("Text")
   
def  Picture():
    print("Picture")

    
root = Tk()
root.title("Welcome to LikeGeeks app")
root.geometry('500x700+100+50')
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="OpenFlie", command=OpenFlie)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

insertpmenu = Menu(menu)
menu.add_cascade(label="Insert", menu=insertpmenu)
insertpmenu.add_command(label="Text", command=Instext)
insertpmenu.add_command(label="Picture", command=Picture)


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
