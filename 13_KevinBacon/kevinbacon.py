from pythonds import Graph, Queue
import sys
from itertools import groupby, permutations
from time import time

start = time()
baconGraph = Graph()

# with open('movie_actors.csv') as cast:
#     prev_movie, actor = cast.readline().strip().split('|')
#     alist = [actor]
#     for line in cast:
#         movie, actor = line.strip().split('|')
#         if movie == prev_movie:
#             alist.append(actor)
#         else:
#             for i in alist:
#                 for j in alist:
#                     if i != j:
#                         baconGraph.addEdge(i,j,prev_movie)
#             prev_movie = movie
#             alist = [actor]

# this is kind of a cool way to do this with the itertools.groupby function.

def rowiter(f):
    for line in f:
        yield line.strip().split('|')

with open('movie_actors.csv') as cast:
    groups = groupby(rowiter(cast), key=lambda x: x[0])
    for movie, group in groups:
        actors = [x[1] for x in group]
        for p in permutations(actors,2):
            baconGraph.addEdge(*p,movie)
end = time()
print("time to build the graph = {}".format(end-start))

kevin = baconGraph.getVertex('Kevin Bacon')

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')

bfs(baconGraph,kevin)

print(kevin)

max = 0
for v in baconGraph:
    if v.dist >= max:
        if v.dist != sys.maxsize:
            max = v.dist
            print(v.id, v.dist)

done = False
while not done:
    actor = input('enter an actor')
    if baconGraph.getVertex(actor):
        start = baconGraph.getVertex(actor)
        while start.pred != None:
            print("{} acted with {} in {}".format(start.id, start.pred.id, start.connectedTo[start.pred]))
            start = start.pred
