from tkinter import *
from tkinter import Menu


class SmileyFace:
    def __init__(self, canvs):
        self.canvas = canvs

        canvas.create_oval(70, 70, 350, 350, fill='yellow')
        canvas.create_oval(125, 125, 175, 175, fill='black', tags='left')
        canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
        canvas.create_line(125, 250, 275, 250, width=5, tags='mouth')

    def smile(self):
        self.canvas.delete('right||mouth')
        self.canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
        self.canvas.create_arc(125, 225, 275, 275, extent=-180, width=5, fill='white', tags='mouth')

    def sad(self):
        self.canvas.delete('right||mouth')
        self.canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
        self.canvas.create_arc(125, 250, 275, 300, extent=180, width=5, fill='white', tags='mouth')

    def wink(self):
        self.canvas.delete('right||mouth')
        self.canvas.create_line(225, 140, 250, 165, 275, 140, width=5, smooth='true', tags='right')
        self.canvas.create_line(125, 250, 275, 250, width=5, tags='mouth')

    def grin(self):
        self.canvas.delete('right||mouth')
        self.canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
        self.canvas.create_line(125, 250, 200, 250, 275, 215, width=5, smooth='true', tags='mouth')


win = Tk()
canvas = Canvas(win, width=800, height=800)
canvas.pack()
smiley = SmileyFace(canvas)

menubar = Menu(win)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Smile", command=smiley.smile)
filemenu.add_command(label="sad", command=smiley.sad)
filemenu.add_command(label="wink", command=smiley.wink)
filemenu.add_command(label="grin", command=smiley.grin)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.destroy)
menubar.add_cascade(label="File", menu=filemenu)
win.config(menu=menubar)

win.mainloop()
