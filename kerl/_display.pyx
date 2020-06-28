import kerl.pixel

cdef class Display:
        def __init__(self, pixel *pixels):
                self.pixels = pixels
        
        def allpixelswereinitalized(self): pass

