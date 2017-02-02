from Truck import *
from Graph import *


def TEST():
    print("Test Start")
    print()
    p = Pos(1,2)
    assert p == p

    v = Vertex(p)
    v.__repr__()
