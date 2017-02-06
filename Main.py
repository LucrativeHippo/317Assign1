from Position import Pos
from Package import Package
from Truck import Truck
from Graph import Edge
from Graph import Vertex
from Graph import Graph
from AStar import *
from random import randrange
from time import time

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


def unit_test():
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


SIZE = 20
NUM_TRUCKS = 3
NUM_PACKS = 15
START_TIME = time()
func_time2 = time()
g = Graph()
for i in range(0, SIZE):
    for j in range(0, SIZE):
        g.add_vertex(Pos(i, j))

func_time = time()
print("Vertex build time: " + str(func_time-func_time2))
func_time2 = time()

for i in range(0, SIZE):
    for j in range(0, SIZE-1):
        g.add_edge(g[Pos(i, j)], g[Pos(i, j+1)])
        g.add_edge(g[Pos(j, i)], g[Pos(j+1, i)])

func_time = time()
print("Edge build time: " + str(func_time-func_time2))
func_time2 = time()

truck_list = list()
for i in range(0, NUM_TRUCKS):
    truck_list.append(Truck(Pos(0, 0)))

func_time = time()
print("Truck build time: " + str(func_time-func_time2))
func_time2 = time()

package_list = list()
for i in range(0, NUM_PACKS):
    package_list.append(Package(Pos(randrange(0, SIZE), randrange(1, SIZE))))

print("Packages: " + str(package_list))

func_time = time()
print("Package build time: " + str(func_time-func_time2))
func_time2 = time()

"""
g.add_edge(g[Pos(0,0)], g[Pos(0,1)])
g.add_edge(g[Pos(0,1)], g[Pos(0,2)])
g.add_edge(g[Pos(0,2)], g[Pos(0,3)])
g.add_edge(g[Pos(1,0)], g[Pos(1,1)])
g.add_edge(g[Pos(1,1)], g[Pos(1,2)])
g.add_edge(g[Pos(1,2)], g[Pos(1,3)])
g.add_edge(g[Pos(2,0)], g[Pos(2,1)])
g.add_edge(g[Pos(2,1)], g[Pos(2,2)])
g.add_edge(g[Pos(2,2)], g[Pos(2,3)])
g.add_edge(g[Pos(3,0)], g[Pos(3,1)])
g.add_edge(g[Pos(3,1)], g[Pos(3,2)])
g.add_edge(g[Pos(3,2)], g[Pos(3,3)])
g.add_edge(g[Pos(0,0)], g[Pos(1,0)])
g.add_edge(g[Pos(1,0)], g[Pos(2,0)])
g.add_edge(g[Pos(2,0)], g[Pos(3,0)])
g.add_edge(g[Pos(0,1)], g[Pos(1,1)])
g.add_edge(g[Pos(1,1)], g[Pos(2,1)])
g.add_edge(g[Pos(2,1)], g[Pos(3,1)])
g.add_edge(g[Pos(0,2)], g[Pos(1,2)])
g.add_edge(g[Pos(1,2)], g[Pos(2,2)])
g.add_edge(g[Pos(2,2)], g[Pos(3,2)])
g.add_edge(g[Pos(0,3)], g[Pos(1,3)])
g.add_edge(g[Pos(1,3)], g[Pos(2,3)])
g.add_edge(g[Pos(2,3)], g[Pos(3,3)])
"""


def solve_prob(graph, trucks, packages):
    """

    :param graph:
    :type graph: Graph
    :param trucks:
    :type trucks: list[Truck]
    :param packages:
    :type packages: list[Package]
    :return:
    :rtype:
    """
    # sort packages descending, distance from garage
    packages.sort(key=lambda temp: get_hcost(trucks[0], temp), reverse=False)
    print(packages)

    start_package = NUM_PACKS%NUM_TRUCKS


    while len(package_list) != 0:
        """
        # leaves the lowest distance packages to be taken last
        if start_package < len(packages):
            trucks.sort(key=lambda temp: temp.distance)
            if trucks[0].lowPackage == False:
                p = packages.pop(start_package-1)
                trucks[0].lowPackage = True
            else:
                p = packages.pop(len(packages) - 1)
                trucks[0].lowPackage = False
            t = trucks[0]

        else:
        """

        # take truck with least travelled distance to pick up furthest package
        trucks.sort(key=lambda temp: temp.distance)
        if trucks[0].lowPackage == False:
            p = packages.pop()
            trucks[0].lowPackage = True
        else:
            p = packages.pop(len(packages)-1)
            trucks[0].lowPackage = False
        t = trucks[0]

        # A* to Package
        path = astar(g[t], g[p])
        if path is None:
            print("No path exists to Package: " + str(p))
        else:
            t.distance += path.gcost*2


solve_prob(g, truck_list, package_list)
print("Solve Time: " + str(time()-START_TIME))
print(truck_list)
# while len(package_list) != 0:
#     print("hi")
#     truck = truck_list.pop(i)
#     x = astar(g[truck], g[package_list[0]])
#     package_list.remove(package_list[0])
#     print("truck " + str(i) + ": steps taken: " + str(x.gcost))
