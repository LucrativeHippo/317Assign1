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

    def __set__(self, instance, value):
        """

        :param instance:
        :type instance:
        :param value:
        :type value: Pos
        :return:
        :rtype:
        """
        self.x = value.x
        self.y = value.y

    def __repr__(self):
        """

        :return: '(x,y)'
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __cmp__(self, other):
        """

        :param other:
        :type other: Pos
        :return:
        :rtype:
        """
        return (self.x == other.x) & (self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))