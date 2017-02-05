from Position import Pos


class Package(Pos):
    def __init__(self, pos):
        """

        :param pos:
        :type pos: Pos
        """
        super().__init__(pos.x, pos.y)
        # self.destination = destination
