import numpy as np
import re
import turtle
import tkinter as tk

lines = np.genfromtxt(
    'test1.iso', delimiter='*', dtype=None, encoding=None)

lib = {
    'x_boundary': 0,
    'y_boundary': 0,
    'M14': 'Knife Down',
    'M15': 'Knife Up'
}

pattern = re.compile("^[X]([0-9]*)[Y]([0-9]*)")
boundaries = re.compile("(.)*[=]([0-9]*.[0-9]*).*[=]([0-9]*.[0-9]*)")

arr = []


def parse(mem):
    if mem == 'M14':
        arr.append(mem)
    elif mem == 'M15':
        arr.append(mem)
    elif pattern.match(mem):
        arr.append([int(pattern.match(mem).group(1)) * 2.54 / 100,
                    int(pattern.match(mem).group(2)) * 2.54 / 100])
    elif boundaries.match(mem):
        lib['x_boundary'] = float(boundaries.match(mem).group(2))
        lib['y_boundary'] = float(boundaries.match(mem).group(3))


for i in lines:
    parse(i)


# start canvas code

root = tk.Tk()
canvas = tk.Canvas(
    master=root, width=lib['x_boundary'] * 2, height=lib['y_boundary'] * 2)
canvas.pack()

t = turtle.RawTurtle(canvas)
screen = turtle.TurtleScreen(canvas)
screen.setworldcoordinates(
    1, 1, lib['x_boundary'] * 2, lib['y_boundary'] * 2)

turtle = turtle.RawTurtle(screen)

frame = tk.Frame(root)

frame.pack(side=tk.TOP, fill=tk.BOTH)


sizeLabel = tk.Label(frame, relief="ridge", text=" Height: {}cm\nWidth: {}cm".format(
    lib['x_boundary'], lib['y_boundary']), fg="red", font="200")

sizeLabel.pack(side="left")

# playground = turtle.Screen()
# playground.setup(width=lib['x_boundary'] * 2,
#                  height=lib['y_boundary'] * 2)
# playground.title("Consult X")

# turtle.Turtle()
# turtle.setworldcoordinates(
#     1, 1, lib['x_boundary'] * 2, lib['y_boundary'] * 2)
# # turtle.tracer(0, 0)           --------INSTANT DARW


def draw(el):
    if el == 'M15':
        turtle.penup()
        # print('M15')
    elif el == 'M14':
        turtle.pendown()
        # print('M14')
    else:
        turtle.goto(el[0] * 2, el[1] * 2)
        # print(el)


for i in arr:
    draw(i)

turtle.mainloop()
