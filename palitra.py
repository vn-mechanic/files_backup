from tkinter import *

root = Tk()
root.geometry("550x200")

def get_color_red(event):
    global COLOR, var
    COLOR[0] = str(event.x)
    ACTUAL_COLOR.configure(background=rgb(tuple([int(i) for i in COLOR])))
    var.set(".".join(COLOR))


def get_color_green(event):
    global COLOR
    COLOR[1] = str(event.x)
    ACTUAL_COLOR.configure(background=rgb(tuple([int(i) for i in COLOR])))
    var.set(".".join(COLOR))


def get_color_blue(event):
    global COLOR
    COLOR[2] = str(event.x)
    ACTUAL_COLOR.configure(background=rgb(tuple([int(i) for i in COLOR])))
    var.set(".".join(COLOR))


def rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


Label(root, text="RED:").grid()
r = Canvas(root, width=255, height=20)
r.grid(row=1)
Label(root, text="GREEN:").grid(row=3)
g = Canvas(root, width=255, height=20)
g.grid(row=4)
Label(root, text="BLUE:").grid(row=5)
b = Canvas(root, width=255, height=20)
b.grid(row=6)

for i in range(256):
    r.create_line(i, 15, i+1, 0, fill=rgb((i, 0, 0)))
    g.create_line(i, 15, i+1, 0, fill=rgb((0, i, 0)))
    b.create_line(i, 15, i+1, 0, fill=rgb((0, 0, i)))






COLOR = ["0", "0", "0"]
var = StringVar()
var.set("0.0.0")
Label(root, text="COLOR:").grid(row=0, column=1)
Label(root, textvariable=var).grid(row=0, column=2)

r.bind("<Button-1>", get_color_red)
g.bind("<Button-1>", get_color_green)
b.bind("<Button-1>", get_color_blue)

ACTUAL_COLOR = Canvas(root, height=40, width=40)
ACTUAL_COLOR.grid(column=1, row=1, columnspan=2)
ACTUAL_COLOR.configure(background="white")


root.mainloop()