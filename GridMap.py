#!/usr/bin/python
# --*coding: utf-8*--

"""file comments here
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'


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
    def getNode(self, x, y):
        return self.__map[x*self.__height+y]

if __name__ == '__main__':
    pass
