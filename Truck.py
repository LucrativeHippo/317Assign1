from Graph import *


class Truck(Pos):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.packs = {}

    def __repr__(self):
        """

        :return: (Packages(pos.x,pos.y))
        """
        return "("+str(self.packs)+super().__repr__()+")"

    def goto(self,pos):
        """
        Takes truck to position 'pos'
        :type pos: Pos
        """
        self.x = pos.x
        self.y = pos.y


