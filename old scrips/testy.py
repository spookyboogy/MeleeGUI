from tkinter import *
from PIL.ImageTk import PhotoImage

def movelbl(event):

    print(event.x, event.y)
    
root = Tk()
canvas = Canvas(root, height = 800, width = 800)
canvas.pack()
img = PhotoImage(file = 'p4coin.png')


lbl = Label(root, image = img)
lbl.pack()
canvas.create_window((200, 200), window = lbl)

lbl.bind('<B1-Motion>',movelbl)
