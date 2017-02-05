from Graph import Vertex
from Graph import Edge
from Graph import Graph
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


class AStarNode:
    def __init__(self, vertex, prev=None, gcost=0, hcost=0):
        """

        :type vertex: Vertex
        :type prev: AStarNode
        :param vertex: Current vertex data
        :param prev: previous AStarNode
        """
        self.vertex = vertex
        self.prev = prev
        self.hcost= hcost
        if prev is None:
            self.gcost = gcost
        else:
            self.gcost = prev.gcost + gcost

    def __cmp__(self,other):
        """

        :type other: AStarNode
        :param other:
        :return:
        """
        return self.vertex.data.__cmp__(other.vertex.data)


def getANode(aList,vertex):
    """

    :type aList: list
    :param aList:
    :type pos: Vertex
    :param pos:
    :return:
    """
    for n in aList:
        if n.vertex.data.__cmp__(vertex.data):
            return n
    return None


def AStar(start, dest):
    """

    :type start: Vertex
    :type dest: Vertex
    :param start: start vertex
    :param dest: destination vertex
    :return: AStarNode with path to dest from start reversed
    """
    node_list = list()

    node_list.append(AStarNode(start))

    while len(node_list) != 0:
        cur_node = node_list.pop()
        print("cur" + str(cur_node))
        if cur_node.vertex.data.__cmp__(dest):
            return cur_node

        for e in cur_node.vertex.edges:
            aTemp = AStarNode(e.nextVertex,
                              cur_node,
                              e.weight,
                              get_hcost(e.nextVertex, dest)
                              )
            inList = getANode(node_list,aTemp.vertex)

            if inList is None:
                node_list.append(aTemp)
            else:
                if aTemp.gcost<inList.gcost:
                    node_list.remove(inList)
#               else: do nothing
        node_list.sort(key=lambda x: x.gcost+x.hcost)



    return cur_node










