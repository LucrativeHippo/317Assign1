from Position import *


class Package(Pos):
    def __init__(self, source, destination):
        """

        :param x: x Position
        :param y: y Position
        """
        self.source = source
        self.destination = destination
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

