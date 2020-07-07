from kerl.display import *

class MenuBar(Display):
	def __init__(self, name):
		self.name = name
		self.items = [MenuBarItem(self, self.name)]
		self.pixels = [pixel for pixel in self.items.pixels]

class MenuBarItemError(Exception):
	''' Raised when athere is an error with a menubar item. '''
	
	pass

class MenuBarItem(Display):
	''' A Menu Bar Item shown in the menubar. '''
	
	def __init__(self, menubar, title):
		if not menubar: # There is no menubar to be displayed on.
			raise MenuBarItemError("There must be a menubar attached/associated with a menu bar item.")
		elif type(menubar) != MenuBar: # The user did nit specify a correct menu bar object.
			raise MenuBarItemError("You must pass a menu bar object to dispoay this menubar object on.")
		
		menubar.items.append(self) # The Menu bar object is attached to this object, and this object is attached to the menu bar object.
		self.menubar = menubar #   ^^
		self.hovered_over = False # When an instance of this object is instantiated, the mouse did not hover.
		self.pixels = []
		
	def _onmousehover(self):
		if not self.hovered_over:
			raise MenuBarItemError("Mouse was not hovered on.")
			else: self.onmousehover() # The mouse was hovered on.
			
	def onmousehover(self):
		''' Executed when a mouse is hovered. '''
		
		pass