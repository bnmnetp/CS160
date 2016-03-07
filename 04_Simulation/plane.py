#!/usr/bin/env python3
import random
import turtle
from pythonds.basic import Queue
import time

# Boarding Strategies
# 1.  All Passengers all random
# 2.  From the back by zone
# 3.  Randomly assigned by zone


class Passenger:
    def __init__(self, row, seat, zone, delay):
        self.row = row
        self.seat = seat
        self.zone = zone
        self.delay = delay

    def __str__(self):
        return "{} {} {}".format(self.row, self.seat, self.delay)

num_rows = 36
num_zones = 6
num_cols = 7

win = turtle.Screen()
win.setup(width=num_rows*20,height=num_cols*20)
win.setworldcoordinates(0,0,num_rows,num_cols)
tlist = []
win.tracer(0)

for i in range(num_rows):
    tlist.append([])
    for j in range(num_cols):
        nt = turtle.Turtle()
        nt.speed(0)
        nt.up()
        nt.goto(i,j)
        nt.shape('square')
        nt.fillcolor('gray')
        tlist[i].append(nt)

win.update()


def timeOneBoarding(num_rows,num_zones,tlist):
    passlist = []
    seatmap = {'a':6, 'b':5,'c':4, 'd':2,'e':1,'f':0}

    for row in range(1, num_rows):
        for seat in "abcdef":
            passlist.append(Passenger(row=row, seat=seat, zone=row // (num_rows // num_zones), delay=random.randrange(1, 6)))
            #passlist.append(Passenger(row=row, seat=seat, zone=random.randrange(num_zones), delay=random.randrange(1, 6)))

    random.shuffle(passlist)
    boardingQueue = Queue()

    for zone in range(num_zones, -1, -1):
        l = [p for p in passlist if p.zone == zone]
        print(len(l))
        for p in l:
            boardingQueue.enqueue(p)

    aisle = [False for i in range(num_rows)]
    simtime = 0
    while not boardingQueue.isEmpty() or (not all([not p for p in aisle])):
        # iterate over the aisle, if a passenger can move towards the back then do it
        # if a passenger can move into their seat and has taken long enough then do it
        # if the opening aisle position is open then fill it from the queue
        for pos in range(len(aisle)-1, 0, -1):
            if aisle[pos] == False:
                if aisle[pos-1] != False and aisle[pos-1].row > pos-1:
                    aisle[pos] = aisle[pos-1]
                    tlist[pos][3].fillcolor('blue')
                    aisle[pos-1] = False
                    tlist[pos-1][3].fillcolor('gray')
            elif aisle[pos].row == pos:
                if aisle[pos].delay == 0:
                    print("seating passenger in row {} seat {}".format(aisle[pos].row, aisle[pos].seat))
                    tlist[aisle[pos].row][seatmap[aisle[pos].seat]].fillcolor('green')
                    aisle[pos] = False
                    tlist[pos][3].fillcolor('gray')
                else:
                    tlist[pos][3].fillcolor('red')
                    aisle[pos].delay -= 1
        if aisle[0] == False:
            if not boardingQueue.isEmpty():
                aisle[0] = boardingQueue.dequeue()

        win.update()
        simtime += 1
        time.sleep(0.1)


    print("Total Boarding Time = {}".format(simtime))
    return simtime

total = 0
for i in range(1):
    total += timeOneBoarding(num_rows,num_zones,tlist)

print("Average = {}".format(total/100))
win.exitonclick()