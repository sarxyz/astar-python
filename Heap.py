#!/usr/bin/python
# -* coding: utf-8 *-

"""Comment.
"""

__author__ = "hjason"
__email__ = "hjason2042@gmail.com"

import sys

def compare_bak(opx, opy):
    """Self-defined compare method"""
    if opx.data > opy.data:
        return 1
    elif opx.data < opy.data:
        return -1
    else:
        return 0

class Heap(object):
    """
    """
    def __init__(self, data = None, pCompareFunc = None):
        if pCompareFunc == None:
            print 'You need a compariable func'
            sys.exit()
        self.pCompareFunc = pCompareFunc
        if data == None:
            self.heap = []
        else:
            self.makeHeap(data)
    def insert(self, element):
        length = len(self.heap)
        self.heap.append(element) # insert backend
        self.__sift_up(length)
    def delete(self, pos):
        if pos >= len(self.heap) or pos < 0:
            return None
        else:
            tmp = self.heap[-1]
            self.heap[-1] = self.heap[pos]
            self.heap[pos] = tmp
            ret = self.heap.pop()
            if (pos+1)/2-1 >= 0 and self.pCompareFunc(self.heap[pos], self.heap[(pos+1)/2-1]) == -1:
                self.__sift_up(pos)
            elif 2*pos+1 < len(self.heap):
                self.__sift_down(pos)
            return ret
    def makeHeap(self, data):
        self.heap = []
        for x in data:
            self.insert(x)
    def printHeap(self):
        print self.heap
    def __sift_down(self, pos):
        i = pos
        flag = True
        while flag and 2*i+1 < len(self.heap):
            smaller = self.heap[2*i+1]
            if 2*i+2 < len(self.heap) and self.pCompareFunc(self.heap[2*i+2], self.heap[2*i+1]) == -1:
                smaller = self.heap[2*i+2]
            if self.pCompareFunc(smaller, self.heap[i]) == -1:
                if self.pCompareFunc(smaller, self.heap[2*i+1]) == 0:
                    tmp = self.heap[2*i+1]
                    self.heap[2*i+1] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2*i+1
                else:
                    tmp = self.heap[2*i+2]
                    self.heap[2*i+2] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2*i+2
            else:
                flag = False
    def __sift_up(self, pos):
        i = pos
        flag = True
        while flag and i > 0:
            if self.pCompareFunc(self.heap[(i+1)/2-1], self.heap[i]) == 1:
                tmp = self.heap[(i+1)/2-1]
                self.heap[(i+1)/2-1] = self.heap[i]
                self.heap[i] = tmp
                i = (i+1)/2-1
            else:
                flag = False

if __name__ == "__main__":
    array = [5, 7, 1, 3, 2, 8, 10]
    heap = Heap(array, compare)
    heap.printHeap()
    heap.delete(2)
    heap.printHeap()
    heap.insert(0)
    heap.printHeap()
