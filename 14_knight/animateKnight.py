def bfs(g,s):
    s.setDistance(0)
    s.setPred(None)
    Q = Queue()
    Q.enqueue(s)
    while (Q.size() > 0):
        w = Q.dequeue()
        for v in w.getConnections():
            if (v.getColor() == 'white'):
                v.setColor('gray')
                v.setDistance( w.getDistance() + 1 )
                v.setPred(w)
                Q.enqueue(v)
        w.setColor('black')#
#  knights
#
#  Created by Brad Miller on 2005-02-26.
#  Copyright (c) 2005 Luther College. All rights reserved.
#

import sys
import os
from dfs import *
from adjGraph import *
from graphics import *
import time

#time = 0

def main():
    ktGraph = Graph()
    # Build the graph
    for row in range(8):
       for col in range(8):
           nodeId = posToNodeId(row,col)
           newPositions = genLegalMoves(row,col)
           for e in newPositions:
               nid = posToNodeId(e[0],e[1])
               ktGraph.addEdge(nodeId,nid)
    posList = []
    start = time.clock()
    res = animateKnight(1,posList,ktGraph.getVertex(10))
    end = time.clock()
    print("search time = ", (end-start))
    for i in posList:
        print(i.id)
    print(res)
    win.getMouse()

def posToNodeId(row,col):
    return (row * 8) + col

def NodeToPos(id):
    return ((id/8, id%8))

def genLegalMoves(x,y):
    newMoves = []
    for i in [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX) and legalCoord(newY):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x):
    if x >= 0 and x < 8:
        return True
    else:
        return False

def orderByAvail(n):
    """
    This function implements a simple heuristic that encourages the search to try the
    nodes with the least available moves FIRST, amazingly this works 1000's of times
    better than choosing the node with the most available moves!  It finds a solution
    in approximately 0.1 seconds as opposed to the 'random' selection method which
    takes 32 minutes!
    """
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    #resList.sort()
    #resList.reverse()
    return [y[1] for y in resList]

win = GraphWin('tour',500,500)
win.setCoords(0,0,8,8)
rList = []
for i in range(8):
    for j in range(8):
        rList.append(Rectangle(Point(i,j),Point(i+1,j+1)))

for i in rList:
    i.draw(win)

def animateKnight(n,path,u):
        rList[u.getId()].setFill('blue')
        time.sleep(0.1)
        u.setColor('gray')
        path.append(u)
        if n < 64:
            pList = orderByAvail(u)
            i = 0
            done = False
            while i < len(pList) and not done:
                if pList[i].getColor() == 'white':
                    done = animateKnight(n+1,path,pList[i])
                i = i + 1
            if not done:  # prepare to backtrack
                path.remove(u)
                u.setColor('white')
                rList[u.getId()].setFill('white')
        else:
            done = True
        return done

if __name__ == '__main__':
    main()
