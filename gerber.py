import numpy as np
import re
import turtle


wn = turtle.Screen()
fred = turtle.Turtle()

lines = np.genfromtxt(
    'mattram-63x63.iso', delimiter='*', dtype=None, encoding=None)

lib = {
    'M14': 'Knife Down',
    'M15': 'Knife Up'
}

pattern = re.compile("^[X]([0-9]*)[Y]([0-9]*)")

arr = []


def parse(mem):
    if mem == 'M14':
        arr.append(mem)
    elif mem == 'M15':
        arr.append(mem)
    elif pattern.match(mem):
        arr.append([pattern.match(mem).group(1), pattern.match(mem).group(2)])


def draw(el):
    if el == 'M15':
        turtle.penup()
    elif el == 'M14':
        turtle.pendown()
    else:
        turtle.goto(el[0], el[1])


for i in lines:
    parse(i)

for i in range(0, arr.length):
    draw(i)
