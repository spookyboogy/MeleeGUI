from tkinter import *
from ttk import *
from PIL.ImageTk import PhotoImage


def changeimage(val):
    
    canvas.delete('weep')
    if val == '0':
        canvas.create_image((500,800), image = img, tag = 'weep')
    else:
        canvas.create_image((800,500), image = img, tag = 'weep')

def callback():
    widget = canvas.find_withtag('button')
    print(widget)
    canvas.itemconfig(widget, height = 80)
    
root = Tk()
canvas = Canvas(root, height = 800, width = 800)
button = Button(root, command = callback)
img = PhotoImage(file = 'titleimage.png')
canvas.create_image((400,400), image = img, tag = 'weep')
canvas.create_window((300, 300), window = button, width = 50, height =50,
                     tag = 'button')


booly = True

root.after(1000, lambda: changeimage('0'))
        
canvas.pack()

root.mainloop()






