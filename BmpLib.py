#!/usr/bin/python
# --*coding: utf-8*--

"""file comments here
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'

from BmpStruct import *

class BmpLib:
    """class comments here
    """

    def __init__(self):
        self.libbmp = CDLL("libbmp.dylib") # mac os x

    def create(self, width, height, depth):
        self.libbmp.bmp_create.restype = POINTER(BMP_FILE)
        self.libbmp.bmp_create.argtypes = [c_uint32, c_uint32, c_uint32]

        self.__bmp_file = self.libbmp.bmp_create(width, height, depth)

    def set_pixel(self, x, y, pixel):
        self.libbmp.bmp_set_pixel.restype = c_bool
        self.libbmp.bmp_set_pixel.argtypes = [POINTER(BMP_FILE), c_uint32, c_uint32, RGB_PIXEL]
        return self.libbmp.bmp_set_pixel(self.__bmp_file, x, y, pixel)

    def save(self, filename):
        self.libbmp.bmp_save.restype = c_bool
        self.libbmp.bmp_save.argtypes = [POINTER(BMP_FILE), c_char_p]
        return self.libbmp.bmp_save(self.__bmp_file, filename)

if __name__ == '__main__':
    libbmp = BmpLib()

    libbmp.create(800, 600, 24)
    for i in range(800):
        for j in range(600):
            libbmp.set_pixel(i, j, white)
    libbmp.save("test.bmp")
