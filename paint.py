from tkinter import *

root = Tk()
key_pressed = False
last_x, last_y = 0, 0

color = "black"
def rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def start_draw(event):
    global last_x, last_y, key_pressed
    if key_pressed:
        frame.create_line(last_x, last_y, event.x, event.y, fill=color)
        last_x, last_y = event.x, event.y
    else:
        key_pressed = True
        last_x, last_y = event.x, event.y


def stop_draw(event):
    print("re")
    global key_pressed
    key_pressed = False


frame = Canvas(root, width=1000, height=600)
frame.configure(background="white")
# frame.focus_set()

root.bind('<Key>', start_draw)
root.bind('<KeyRelease>', stop_draw)


frame.grid()




root.mainloop()
