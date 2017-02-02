class Pos(object):
    """
    Position class
    """
    def __init__(self, x, y):
        """
        Position for graph
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """

        :return: '(x,y)'
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"



