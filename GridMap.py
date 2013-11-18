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
        self._width = width
        self._height = height
        self._map = data

    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def getNode(self, x, y):
        return self._map[x*self._height+y]

if __name__ == '__main__':
    pass
