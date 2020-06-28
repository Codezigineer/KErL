from kerl.canvas import *

class WidgetError(Exception): pass #Raised when there is an error with a widget.

class Widget(object):
	''' A Widget object. '''
	
	def __init__(self, canvas=Canvas, parent=None, children=[]):
		self.canvas = canvas
		self.parent = parent
		self.children = children
	
	def add_child(self, child):
		if child == self:
			raise WidgetError("Widgets Never get added as a child to themselves.")
		elif type(child) != Widget:
			raise WidgetError("You must add a Widget object as a child to a widget.")
		if child.canvas.width > self.canvas.width:
			self.canvas.width += child.canvas.widget # Then, The window will not look weird and will not be wider than this widget.
		elif child.canvas.height > self.canvas.height: 
			self.canvas.height += self.canvas.height # Then, The window will not look weird and will not be taller than this widget.
		
		self.children.append(child)
