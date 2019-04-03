from tkinter import *
import math

s = 100

phi = 90
x, y = 0, 0

root = Tk()

canvas = Canvas(root)

canvas.pack()


def draw_square(a, b, c, d):
    canvas.create_line(a[0], a[1], b[0], b[1])
    canvas.create_line(b[0], b[1], c[0], c[1])
    canvas.create_line(c[0], c[1], d[0], d[1])
    canvas.create_line(d[0], d[1], a[0], a[1])


# 212.13203435596427-212.13203435596424j
def rotate(a, b, c, d):
    print(a, b, c, d)
    coordinates = [a, b, c, d]
    p = 90
    for i in range(len(coordinates)):
        coordinates[i] = [coordinates[i][0] * math.cos(p) - coordinates[i][1] * math.sin(p) + 200,
                          coordinates[i][0] * math.sin(p) + coordinates[i][1] * math.cos(p) + 200]
    a, b, c, d = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    draw_square(a, b, c, d)


lst = [[10, 10], [100, 10], [100, 100], [10, 100]]

draw_square(*lst)

rotate(*lst)

root.mainloop()
