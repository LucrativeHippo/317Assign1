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
        self.distance = 0
        self.location = pos

    def __repr__(self):
        """

        :return: (Packages(pos.x,pos.y))
        """
        return "(Packs:"+str(self.packs)+" Pos:"+super().__repr__()+" Odo:"+str(self.distance)+")"

    # def pickup(self, pack):
    #     """
    #
    #     :param pack:
    #     :type pack: Package
    #     :return:
    #     :rtype:
    #     """
    #     if self.__cmp__(pack):
    #         self.packs = pack
    #     else:
    #         print("Tried to pickup package when on a different point")
    #
    # def goto(self, pos):
    #     """
    #     Points truck position to 'pos'
    #     :type pos: Pos
    #     """
    #     self.distance += 1
    #     self.x = pos.x
    #     self.y = pos.y


