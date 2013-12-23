#!/usr/bin/python
# --*coding: utf-8*--

"""We use libbmp (written in C) to read or write bmp files.
Now, we call c code via ctypes, which should be changed later.
Data structures are defined in this file.
"""
__author__ = 'hjason'
__email__ = 'hjason2042@gmail.com'

from ctypes import *

class RGB_PIXEL(Structure):
    _fields_ = [("BLUE", c_uint8),
               ("GREEN", c_uint8),
               ("RED", c_uint8),
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

BLUE = RGB_PIXEL(0xe1, 0x69, 0x41, 0)
GREEN = RGB_PIXEL(0, 0xff, 0, 0)
RED = RGB_PIXEL(0, 0, 0xff, 0)

BLACK = RGB_PIXEL(0, 0, 0, 0)
WHITE = RGB_PIXEL(0xff, 0xff, 0xff, 0)
YELLOW = RGB_PIXEL(0x0, 0xff, 0xff, 0)
GREY = RGB_PIXEL(0xbe, 0xbe, 0xbe, 0)

if __name__ == '__main__':
    pass