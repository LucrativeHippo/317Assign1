from Position import Pos
from Package import Package
from Truck import Truck
from Graph import Edge
from Graph import Vertex
from Graph import Graph
from AStar import *

def getVertexByPos(g,x,y):
    """

    :param g:
    :type g: Graph
    :param x:
    :param y:
    :return:
    :rtype:
    """
    return g[Pos(x, y)]



print("Test Start")
print("Position Tests:", end=" ")
p = Pos(1, 2)
assert p.x == 1
assert p.y == 2
assert p == p
assert str(p) == "(1,2)"
print("Passed")

print("Package Tests:", end=" ")
pack = Package(p)
assert pack.x == p.x
assert pack.y == p.y
assert pack == pack
assert str(pack) == "(1,2)"
print("Passed")

print("Truck Tests:", end=" ")
t = Truck(p)
assert t.x == p.x
assert t.y == p.y
assert t == t
assert str(t) == "(None(1,2))"
print("Passed")

print("Trucks & Packages:", end=" ")
assert t.x == pack.x
assert t.y == pack.y
assert t.__cmp__(pack)
#   PICK UP PACKAGE
t.pickup(pack)
assert t.packs is not None
assert t.packs == pack
#   MOVE POSITION
t.goto(Pos(2,1))
print("Passed")

print("Vertex Tests:", end=" ")
v = Vertex(Pos(0, 0))
assert v.data.__cmp__(Pos(0, 0))
print(v.edges)
assert v.edges == []
assert len(v.edges) == 0
print("Passed")

print("Edge Tests:", end=" ")
#   SIMPLE EDGE TEST
e = Edge(v, 4)
assert e.weight == 4
assert e.nextVertex == v
#   ADD EDGE POINT
v2 = Vertex(Pos(1, 0))
v.add_edge(v2,1)
assert v.edges[0].weight == 1
assert v.edges[0].nextVertex == v2
assert len(v.edges) == 1
print("Passed")
del v
del v2

print("Graph Tests:", end=" ")
g = Graph()
for i in range(0, 3):
    for j in range(0, 3):
        g.add_vertex(Pos(i, j))


print(getVertexByPos(g, 0, 0))

print("Passed")


g.add_edge(g[Pos(0,0)], g[Pos(0,1)])

x=AStar(g[Pos(0,0)], g[Pos(0,0)])

print(x)
