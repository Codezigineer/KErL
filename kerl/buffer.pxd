from KErL._type import *
from KErL.kerl.errors import *

cpdef class Buffer(Type):
	''' A class for making buffers. '''
	
	def __init__(self, list array, int count):
		self.array = array
		self.count = count
		
		if self.array[self.count] == None:
			
	def buffer_read(self, int idx):
		return self.array[idx]