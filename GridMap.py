#!/usr/bin/python
# --*coding: utf-8*--

"""file comments here
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'

from BmpLib import *
from BmpStruct import *

class GridMap(object):
    """class comments here
    """

    def __init__(self, width, height, data):
        self.__width = width
        self.__height = height
        self.__map = data

    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def getMap(self):
        return self.__map
    def getNode(self, x, y):
        return self.__map[x+y*self.__width]
    def setNode(self, x, y, value):
        self.__map[x+y*self.__width] = value
    #debug
    def printMap(self):
        width = self.getWidth()
        height = self.getHeight()
        for j in range(height):
            for i in range(width):
                print self.getNode(i, j),
            print ''

    def write_bmp(self, depth, scale, filename):
        """Color definition
start       green   2
goal        red     3
path        blue    4

obstacle    black   9
non-obst    white   1
"""
        width = self.getWidth()
        height = self.getHeight()
        libbmp = BmpLib()
        libbmp.create(width*scale, height*scale, depth)
        for j in range(height*scale):
            for i in range(width*scale):
                if i%scale<2 or j%scale<2:
                    libbmp.set_pixel(i, j, black)
                elif self.getNode(i/scale, j/scale) == 1:
                    libbmp.set_pixel(i, j, white)
                elif self.getNode(i/scale, j/scale) == 2:
                    libbmp.set_pixel(i, j, green)
                elif self.getNode(i/scale, j/scale) == 3:
                    libbmp.set_pixel(i, j, red)
                elif self.getNode(i/scale, j/scale) == 4:
                    libbmp.set_pixel(i, j, blue)
                else:
                    libbmp.set_pixel(i, j, grey)
        libbmp.save(filename)

if __name__ == '__main__':
    pass
