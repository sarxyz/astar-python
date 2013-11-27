#!/usr/bin/python
# --*coding: utf-8*--

"""file comments here
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'

import sys
from ctypes import *

class RGB_PIXEL(Structure):
    _fields_ = [("blue", c_uint8),
               ("green", c_uint8),
               ("red", c_uint8),
               ("alpha", c_uint8)]

class BMP_HEADER(Structure):
    _fields_ = [("magic", c_uint8*2),
               ("filesz", c_uint32),
               ("creator1", c_uint16),
               ("creator2", c_uint16),
               ("offset", c_uint32)]

class BMP_DIB_V3_HEADER(Structure):
    _fields_ = [("header_sz", c_uint32),
               ("width", c_uint32),
               ("height", c_uint32),
               ("nplanes", c_uint16),
               ("depth", c_uint16),
               ("compress_type", c_uint32),
               ("bmp_bytesz", c_uint32),
               ("hres", c_uint32),
               ("vres", c_uint32),
               ("ncolors", c_uint32),
               ("nimpcolors", c_uint32)]

class BMP_FILE(Structure):
    _field_ = [("header", BMP_HEADER),
               ("dib", BMP_DIB_V3_HEADER),
               ("pixels", POINTER(POINTER(RGB_PIXEL))),
               ("colors", POINTER(RGB_PIXEL))]
def test():
    libbmp = CDLL("libbmp.dylib")

    # libbmp.bmp_print_pixel.argtypes = [RGB_PIXEL]
    # libbmp.bmp_print_pixel_by_pointer.argtypes = [POINTER(RGB_PIXEL)]
    # libbmp.bmp_return_pixel_pointer.restype = POINTER(RGB_PIXEL)
    libbmp.bmp_create.restype = POINTER(BMP_FILE)
    libbmp.bmp_create.argtypes = [c_uint32, c_uint32, c_uint32]
    libbmp.bmp_set_pixel.restype = c_bool
    libbmp.bmp_set_pixel.argtypes = [POINTER(BMP_FILE), c_uint32, c_uint32, RGB_PIXEL]
    libbmp.bmp_save.restype = c_bool
    libbmp.bmp_save.argtypes = [POINTER(BMP_FILE), c_char_p]

    pixel = RGB_PIXEL(0x30, 0x0, 0x0, 0xff)
    # libbmp.bmp_print_pixel(pixel)
    # libbmp.bmp_print_pixel_by_pointer(byref(pixel))
    # ret = libbmp.bmp_return_pixel_pointer()
    # libbmp.bmp_print_pixel_by_pointer(ret)

    bmp_file = libbmp.bmp_create(1000, 1000, 1)
    for i in range(1000):
        for j in range(1000):
            ret = libbmp.bmp_set_pixel(bmp_file, i, j, pixel)
    ret = libbmp.bmp_save(bmp_file, "test.bmp")
    print ret


if __name__ == '__main__':
    test()