from kerl.color import *

cdef class Pixel:
        def __init__(self, RGBAColor color):
                self.color = color