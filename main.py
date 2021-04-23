# https://en.wikipedia.org/wiki/Turtle_graphics

from turtle import Turtle, Screen
import random
from time import sleep

COLORS = ["red", "purple", "blue", "green", "orange", "yellow"]
MAX_DISTANCE = 300

t = Turtle()
t.speed(8)
t.width(5)

# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# sleep(2)

s = t.getscreen()
s.bgcolor("black")

# for _ in range(2):
#     i = 0
#     for color in COLORS:
#         i += 1
#         print(color)
#         t.color(color)
#         t.forward(i * 20)
#         t.left(90)

# sleep(2)
# t.clear()

# i = 0
# color = ""
# color_tmp = ""
# while abs(t.xcor()) < MAX_DISTANCE:
#     while color == color_tmp:
#         color_tmp = random.choice(COLORS)
#     color = color_tmp
#     print(color)
#     t.color(color)
#     t.forward(i * 2)
#     t.left(45)
#     i += 1

# t.penup()
# t.home()
# t.clear()
# t.pendown()

# for n in range(360):
#     t.pencolor(COLORS[n%6])
#     t.width(n/100 + 1)
#     t.forward(n)
#     t.left(59)

# sleep(2)
t.clear()

FINISH_LINE = 250
# Draw finish line
t.penup()
t.setpos(FINISH_LINE,300)
t.color("white")
t.pendown()
t.setpos(FINISH_LINE,-300)
t.penup()

turtle_attributes = [
    {
        "shape": "triangle",
        "color": "cyan",
    },
    {
        "shape": "turtle",
        "color": "hot pink",
    },
]

turtles = []

for ta in turtle_attributes:
    t = Turtle()
    t.shape(ta["shape"])
    t.color(ta["color"])
    turtles.append(t)

i = 0
for t in turtles:
    t.penup()
    t.setpos(-300, 50 + (i * -100))
    i += 1

while turtles[0].xcor() < FINISH_LINE and turtles[1].xcor() < FINISH_LINE:
    for t in turtles:
        t.forward(random.randint(0,10))
        sleep(random.random())

print("DONE")