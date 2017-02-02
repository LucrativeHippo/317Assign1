from Position import *


class Truck(Pos):
    def __init__(self, x, y):
        self.pos = super.__init__(x, y)
        self.pos = Pos(x, y)

    def __repr__(self):
        """

        :return: (Packages(pos.x,pos.y))
        """
        return "("+str(self.packs)+self.pos.__repr__()+")"

    def goto(self, pos):
        """
        Points truck position to 'pos'
        :type pos: Pos
        """
        self.pos = pos
