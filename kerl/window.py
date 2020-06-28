from kerl.widget import *
from kerl.canvas import *

class Window(Widget):
	''' A Window. '''
	
	def __init__(self, canvas=Canvas, windowname="Window", parent=None):
		super().__init__(canvas=canvas, parent=parent)
		self.windowname = windowname
