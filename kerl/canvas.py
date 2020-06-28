class Canvas(object):
	''' A canvas describing the rules of how a widget is displayed in size and area. '''
	
	def __init__(self, x=0, y=0, width=0, height=0):
		self.x = x
		self.y = y
		self.width = width
		self.height = height