#!/usr/bin/env python3
import random
from pythonds.basic import Queue

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

def timeOneBoarding(num_rows,num_zones):
    passlist = []

    for row in range(1, num_rows):
        for seat in "abcdef":
            passlist.append(Passenger(row=row, seat=seat, zone=row//(num_rows//num_zones), delay=random.randrange(1, 6)))

    random.shuffle(passlist)
    boardingQueue = Queue()

    for zone in range(num_zones, -1, -1):
        l = [p for p in passlist if p.zone == zone]
        print(len(l))
        for p in l:
            boardingQueue.enqueue(p)

    aisle = [False for i in range(num_rows)]
    time = 0
    while not boardingQueue.isEmpty() or (not all([not p for p in aisle])):
        # iterate over the aisle, if a passenger can move towards the back then do it
        # if a passenger can move into their seat and has taken long enough then do it
        # if the opening aisle position is open then fill it from the queue
        for pos in range(len(aisle)-1, 0, -1):
            if aisle[pos] == False:
                if aisle[pos-1] != False and aisle[pos-1].row > pos-1:
                    aisle[pos] = aisle[pos-1]
                    aisle[pos-1] = False
            elif aisle[pos].row == pos:
                if aisle[pos].delay == 0:
                    print("seating passenger in row {} seat {}".format(aisle[pos].row, aisle[pos].seat))
                    aisle[pos] = False
                else:
                    aisle[pos].delay -= 1
        if aisle[0] == False:
            if not boardingQueue.isEmpty():
                aisle[0] = boardingQueue.dequeue()

        time += 1


    print("Total Boarding Time = {}".format(time))
    return time

total = 0
for i in range(100):
    total += timeOneBoarding(num_rows,num_zones)

print("Average = {}".format(total/100))