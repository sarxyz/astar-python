#!/usr/bin/python
# --*coding: utf-8*--

"""file comments here
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'

from GridMap import GridMap

class GridNode(object):
    """class comments here
    """

    def __init__(self, map=None, x=0, y=0):
        self.__map = map
        self.__xPos = x
        self.__yPos = y
    def getX(self):
        return self.__xPos
    def getY(self):
        return self.__yPos
    def getAccessAttribute(self):
        if self.__map == None:
            return False
        else:
            width = self.__map.getWidth()
            height = self.__map.getHeight()
            if self.__xPos < 0 or self.__xPos >= width or self.__yPos < 0 or self.__yPos >= height:
                return False
            else:
                return self.__map.getNode(self.__xPos, self.__yPos)==9
    def getCost(self):
        return self.__map.getNode(self.__xPos, self.__yPos)

    def isSameNode(self, rhs):
        if self.__map == rhs.__map and self.__xPos == rhs.__xPos and self.__yPos == self.__yPos:
            return True
        return False

    def printNode(self):
        print '<%d, %d>'%(self.__xPos, self.__yPos)


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
    gridNode = GridNode(gridMap, 1, 1)
    print gridNode.getAccessAttribute()
