#!/usr/bin/python
# --*coding: utf-8*--

"""file comments here
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'

import sys

from GridMapData import *
from GridMap import GridMap
from GridNode import GridNode
from Heap import Heap

def getHeuristicCost(a, b):
    """Manhattan
    parameter: a and b both kind of GridNode
    """
    return abs(a.getX()-b.getX()) + abs(a.getY()-b.getY())

def compare(opx, opy):
    """Self-defined compare function for type of PathNode
    """
    if opx.f > opy.f:
        return 1
    elif opx.f < opy.f:
        return -1
    else:
        return 0

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
        self.__start = PathNode(None, start, goal)
        self.__goal = goal
        self.__mOpenList = [] # heap
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
        self.__mOpenList = Heap(None, compare)
        self.__mOpenList.insert(node)
        while True:
            # pop the node which has the smallest f
            cur = self.__mOpenList.delete(0)
            if cur == None: # the heap is empty
                return False
            if cur.gridNode.isSameNode(self.__goal): # success
                self.__mClosedList.append(cur)
                return True
            self.__mClosedList.append(cur)
            candidates = self.get_successors(cur.gridNode)
            # check if the node in closed list or not
            for candidate in candidates:
                i = 0
                length = len(self.__mClosedList)
                while i<length:
                    if candidate.isSameNode(self.__mClosedList[i].gridNode):
                        break
                    i = i+1
                if i<length: # already in closed list, ignore it
                    continue
                # check if the node in open list or not
                j = 0
                length = len(self.__mOpenList.heap)
                while j<length:
                    if candidate.isSameNode(self.__mOpenList.heap[j].gridNode):
                        break
                    j = j+1
                if j<length: # already in open list,
                    new_pathNode = PathNode(cur, candidate, self.__goal)
                    if new_pathNode.g < self.__mOpenList.heap[j].g:
                        self.__mOpenList.delete(j)
                        self.__mOpenList.insert(new_pathNode)
                else:
                    new_pathNode = PathNode(cur, candidate, self.__goal)
                    self.__mOpenList.insert(new_pathNode)
    def print_path(self):
        path = []
        if not self.__mClosedList[-1].gridNode.isSameNode(self.__goal):
            print 'Path not found'
        else:
            parent = self.__mClosedList[-1]
            path.insert(0, parent)
            while True:
                if parent.gridNode.isSameNode(self.__start.gridNode):
                    path.insert(0, parent)
                    break
                else:
                    for x in self.__mClosedList:
                        if parent.gridNode.isSameNode(x.gridNode):
                            path.insert(0, parent)
                            parent = x.parent
            for x in path:
                x.gridNode.printNode()

    def get_pathMap(self):
        pathMap = self.__gridMap
        if not self.__mClosedList[-1].gridNode.isSameNode(self.__goal):
            print 'Path not found'
            return None
        else:
            parent = self.__mClosedList[-1]
            pathMap.setNode(parent.gridNode.getX(), parent.gridNode.getY(), 3)
            parent = parent.parent
            while True:
                if parent.gridNode.isSameNode(self.__start.gridNode):
                    pathMap.setNode(parent.gridNode.getX(), parent.gridNode.getY(), 2)
                    break
                else:
                    for x in self.__mClosedList:
                        if parent.gridNode.isSameNode(x.gridNode):
                            pathMap.setNode(parent.gridNode.getX(), parent.gridNode.getY(), 4)
                            parent = x.parent
            return pathMap

if __name__ == '__main__':
    width = 40
    height = 40
    wall_freq = 0.1
    generator = GenerateGridMapData()
    (data, start, goal) = generator.init(width, height, wall_freq)
    gridMap = GridMap(width, height, data)
    gridMap.write_bmp(24, 16, 'map.bmp')
    startNode = GridNode(gridMap, start%width, start/width)
    goalNode = GridNode(gridMap, goal%width, goal/width)
    astarSearch = AStarSearch(gridMap, startNode, goalNode)
    if astarSearch.find_path():
        path_map = astarSearch.get_pathMap()
        path_map.write_bmp(24, 16, 'path.bmp')
    else:
        print 'Path not found'
