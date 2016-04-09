#!/usr/bin/env python
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press space bar
 ---------------------------------------
"""
from turtle import onkey, clear, write, hideturtle, penup, goto, bye,  listen, mainloop, Turtle

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/6., 0, 1-n/6.)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def moveTower(fromTower, toTower):
    toTower.push(fromTower.pop())

def hanoi(n, fromTower, toTower, usingTower):
    if n > 0:
        hanoi(n - 1, fromTower, usingTower, toTower)
        moveTower(fromTower, toTower)
        hanoi(n - 1, usingTower, toTower, fromTower)

def play():
    onkey(bye,"space")
    clear()
    hanoi(6, t1, t3, t2)
    write("press space bar to exit",
              align="center", font=("Courier", 16, "bold"))

def main():
    global t1, t2, t3
    hideturtle(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(6,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")
    listen()
    return "ALL DONE"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()
