from Graph import *


class Package(Pos):
    def __init__(self,x,y):
        """

        :param x: x Position
        :param y: y Position
        """
        super().__init__(x,y)
        self.carried = False
        self.delivered = False

    def pickup(self):
        """
        Marks package as carried and returns reference to self
        :return: self
        """
        self.carried = True
        return self

    def dropoff(self):
        """

        :return:
        """
        self.carried = False
        self.delivered = True

