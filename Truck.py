from Position import Pos
from Package import Package


class Truck(Pos):
    def __init__(self, pos, packs=None):
        """

        :param pos:
        :type pos: Pos
        :param packs:
        :type packs: Package
        """
        super().__init__(pos.x, pos.y)
        self.packs = packs

    def __repr__(self):
        """

        :return: (Packages(pos.x,pos.y))
        """
        return "("+str(self.packs)+super().__repr__()+")"

    def pickup(self, pack):
        """

        :param pack:
        :type pack: Package
        :return:
        :rtype:
        """
        if self.__cmp__(pack):
            self.packs = pack
        else:
            print("Tried to pickup package when on a different point")

    def goto(self, pos):
        """
        Points truck position to 'pos'
        :type pos: Pos
        """
        self.x = pos.x
        self.y = pos.y
        self.packs.x = pos.x
        self.packs.y = pos.y

