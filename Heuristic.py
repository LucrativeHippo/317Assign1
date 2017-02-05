
from Position import Pos
import math


def get_hcost(start, dest):
    """

    :type start: Pos
    :type dest: Pos
    :param start:
    :param dest:
    :return: heuristic cost from start to dest
    """
#   Straight line distance
    return math.sqrt(math.pow((start.x-dest.x), 2) + math.pow((start.y-dest.y), 2))
#   Boardwalk distance
#   return abs(start.x-dest.x)+abs(start.y-dest.y)