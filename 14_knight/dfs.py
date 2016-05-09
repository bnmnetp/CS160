# DFS implementation using adjGraph where nodes contain an adj list reference to other nodes # from stack

from adjGraph import *

time = 0

def dfs(theGraph):
    for u in theGraph:
        u.setColor('white')
        u.setPred(-1)
    time = 0
    for u in theGraph:
        if u.getColor() == 'white':
            time = dfsvisit(u,time)

def dfsvisit(u, time):
    print("visiting: ",u,"at ", time)
    u.setColor('gray')
    time = time+1
    u.setDiscovery(time)
    for v in u.getConnections():
        if v.getColor() == 'white':
            v.setPred(u)
            time = dfsvisit(v,time)
    u.setColor('black')
    time = time + 1
    u.setFinish(time)
    return time


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

def dfsiter(s):
    s.setDistance(0)
    s.setPred(None)
    S = Stack()
    S.push(s)
    while (S.size() > 0):
        w = S.pop()
        w.setColor('gray')
        for v in w.getConnections():
            if (v.getColor() == 'white'):
                v.setDistance( w.getDistance() + 1 )
                v.setPred(w)
                S.push(v)
        w.setColor('black')

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
#    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]   

def knightTour(n,path,u,limit,so):
        so.calls += 1
        if so.calls > 1000000000:
            n = limit
        u.setColor('gray')
        path.append(u)
        if n < limit:
#            nbrList = list(u.getConnections())
#            nbrList.sort(key=lambda x: x.id)
            nbrList = orderByAvail(u)            
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1,path,nbrList[i],limit,so)
                i = i + 1
            if not done:  # prepare to backtrack
                if len(path) - 1 - path.index(u) != 0:
                    print('oh oh, not popping the right node')
                path.pop()
                u.setColor('white')
        else:
            done = True
        if n == limit or path == []:
            print ('number of calls = ', so.calls)
        return done


def makeGraph():
    gFile = open("fig714.dat")
    tGraph = DFSGraph()
    for line in gFile:
        fVertex, tVertex = line.split('|')
        fVertex = int(fVertex)
        tVertex = int(tVertex)
        tGraph.addEdge(fVertex,tVertex)
    return tGraph


# dGraph = makeGraph()
# dGraph.dfs()

# for i in dGraph:
#     adj = i.getConnections()
#     for k in adj:
#         print(i, k)


# Local Variables:
# py-which-shell: "python3.2" 
# End:
