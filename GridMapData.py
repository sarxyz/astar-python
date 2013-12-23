#!/usr/bin/python
# --*coding: utf-8*--

"""file comments here
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'

import random

class GenerateGridMapData:
    """generate grid map dada
    """
    def __init__(self):
        random.seed()

    def reset(self):
        random.seed()

    def init(self, width, height, freq):
        n_blocks = int(freq * width * height)
        node_list = random.sample(range(width * height), n_blocks + 2) # 2: start and goal node

        self.__width = width
        self.__height = height
        self.__n_blocks = n_blocks
        gridMapData = [1 for x in range(width * height)]
        for x in range(n_blocks):
            gridMapData[node_list[x]] = 9 # wall
        gridMapData[node_list[n_blocks]] = 2 # start
        gridMapData[node_list[n_blocks + 1]] = 3 # goal
        return (gridMapData, node_list[n_blocks], node_list[n_blocks + 1])

if __name__ == '__main__':
    pass
