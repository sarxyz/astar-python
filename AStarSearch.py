#!/usr/bin/python
# --*coding: utf-8*--

"""file comments here
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'

from GridMap import GridMap
from GridNode import GridNode
from Heap import Heap

def getHeuristicCost(a, b):
    """Manhattan
    parameter: a and b both kind of GridNode
    """
    return abs(a.getX()-b.getX()) + abs(a.getY()-b.getY())


class PathNode(object):
    """
    """
    def __init__(self, parent, node, goal):
        self.parent = parent
        self.gridNode = node
        self.child = None
        if parent == None:
            self.g = 0
            self.h = 0
            self.f = 0
        else:
            self.g = self.parent.g + self.gridNode.getCost()
            self.h = getHeuristicCost(self.gridNode, goal)
            self.f = self.g + self.h




class AStarSearch(object):
    """class comments here
    """
    def __init__(self, gridMap, start, goal):
        """
        @param start: start node(GridNode)
        @param goal: goal node(GridNode)
        """
        self.__gridMap = gridMap
        self.__start = PathNode(None, start)
        self.__goal = goal
        self.__mOpenList = []
        self.__mClosedList = []
        self.__width = self.__gridMap.getWidth()
        self.__height = self.__gridMap.getHeight()

    def get_successors(self, node):
        """ find successor.
        """
        successors = []
        x = node.getX()
        y = node.getY()
        # left
        if not x-1 < 0:
            node = GridNode(self.__gridMap, x-1, y)
            if node.getAccessAttribute():
                successors.append(node)
        # up
        if not y-1 < 0:
            node = GridNode(self.__gridMap, x, y-1)
            if node.getAccessAttribute():
                successors.append(node)
        # right
        if x+1 < self.__width:
            node = GridNode(self.__gridMap, x+1, y)
            if node.getAccessAttribute():
                successors.append(node)
        # down
        if y+1 < self.__height:
            node = GridNode(self.__gridMap, x, y+1)
            if node.getAccessAttribute():
                successors.append(node)
        return successors

    def find_path(self):
        node = self.__start
        self.__mOpenList.append(node)
        self.__mOpenList = Heap(self.__mOpenList).heap
        while self.__mOpenList:
            cur = self.__mOpenList[0]
            self.__mOpenList.remove(0)
            self.__mOpenList = Heap(self.__mOpenList).heap
            self.__mClosedList.append(cur)
            candidates = self.get_successors(cur)
            # check if the node in closed list or not
            for candidate in candidates:
                i = 0
                length = len(self.__mClosedList)
                while i<length:
                    if candidate.gridNode.isSameNode(self.__mClosedList[i].gridNode):
                        break
                if i<length: # already in closed list, ignore it
                    break
            # check if the node in open list or not
            for candidate in candidates:
                i = 0
                length = len(self.__mOpenList)
                while i<length:
                    if candidate.gridNode.isSameNode(self.__mOpenList[i].gridNode):
                        break
                if i<length: # already in open list,
                    pathNode = PathNode(cur, candidate, self.__goal)


                else:
                    pass
            


if __name__ == '__main__':
    width = 20
    height = 20
    # 20*20
    global_map = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                  1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,
                  1,9,9,1,1,9,9,9,1,9,1,9,1,9,1,9,9,9,1,1,
                  1,9,9,1,1,9,9,9,1,9,1,9,1,9,1,9,9,9,1,1,
                  1,9,1,1,1,1,9,9,1,9,1,9,1,1,1,1,9,9,1,1,
                  1,9,1,1,9,1,1,1,1,9,1,1,1,1,9,1,1,1,1,1,
                  1,9,9,9,9,1,1,1,1,1,1,9,9,9,9,1,1,1,1,1,
                  1,9,9,9,9,9,9,9,9,1,1,1,9,9,9,9,9,9,9,1,
                  1,9,1,1,1,1,1,1,1,1,1,9,1,1,1,1,1,1,1,1,
                  1,9,1,9,9,9,9,9,9,9,1,1,9,9,9,9,9,9,9,1,
                  1,9,1,1,1,1,9,1,1,9,1,1,1,1,1,1,1,1,1,1,
                  1,9,9,9,9,9,1,9,1,9,1,9,9,9,9,9,1,1,1,1,
                  1,9,1,9,1,9,9,9,1,9,1,9,1,9,1,9,9,9,1,1,
                  1,9,1,9,1,9,9,9,1,9,1,9,1,9,1,9,9,9,1,1,
                  1,9,1,1,1,1,9,9,1,9,1,9,1,1,1,1,9,9,1,1,
                  1,9,1,1,9,1,1,1,1,9,1,1,1,1,9,1,1,1,1,1,
                  1,9,9,9,9,1,1,1,1,1,1,9,9,9,9,1,1,1,1,1,
                  1,1,9,9,9,9,9,9,9,1,1,1,9,9,9,1,9,9,9,9,
                  1,9,1,1,1,1,1,1,1,1,1,9,1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
    gridMap = GridMap(20, 20, global_map)
    startNode = GridNode(gridMap, 1, 1)
    goalNode = GridNode(gridMap, 19, 15)
    astarSearch = AStarSearch(gridMap, startNode, goalNode)

    astarSearch.find_path()
