from KErL._type import *

cpdef class Canvas(Type):
	''' A canvas describing the rules of how a widget is displayed in size and area. '''
	
	def __init__(self, int x=0, int y=0, int width=0, int height=0):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
