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

    def __repr__(self):
        return str(self.vertex) + "<-" + str(self.prev)


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
    node_list = [AStarNode(start)]
    visited_list = dict()
    cur_node = None

    while len(node_list) != 0:
        cur_node = node_list.pop()
        visited_list[str(cur_node.vertex.data)] = True
        # print("cur" + str(cur_node))
        if cur_node.vertex.data.__cmp__(dest):
            return cur_node

        for e in cur_node.vertex.edges:
            # if the next node has not been visited: visit it
            if visited_list.get(str(e.nextVertex.data)) is None:

                # Create a new node to visit
                aTemp = AStarNode(e.nextVertex,
                                  cur_node,
                                  e.weight,
                                  get_hcost(e.nextVertex, dest)
                                  )
                # get aTemp from node_list
                inList = getANode(node_list, aTemp.vertex)
                if inList is None:  # haven't visited node yet
                    #  add it to the list
                    node_list.append(aTemp)
                else:  # have visited node
                    # check which path is better
                    if aTemp.gcost < inList.gcost:
                        # replace if it is better
                        node_list.remove(inList)
    #               else: do nothing
        print(node_list)
        node_list.sort(key=lambda x: x.gcost+x.hcost, reverse=True)
        print(node_list)

    # The completed Astar did reveal the correct path
    if cur_node.vertex.data.__cmp__(dest):
        return cur_node
    else:  # No path from Start to Destination
        return None










