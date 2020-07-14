from kerl.mainloop import *
from kerl.errors import *
import sys
import os
from kerl._type import *

class Application(MainLoop, Type):
	''' An Application object representing an application. '''
	
	def __init__(self, window, icon=os.path.join(os.path.dirname(__file__), 'icon.png')):
		if window is None:
			InternalError("No window specified.")
		elif type(window) != Window:
			InternalError("Not a window.")
		super().__init__()
		self.argc = sys.argc
		self.argv = sys.argv
		self.env = os.environ
		self.xwindowsystem = True if os.environ['DISPLAY'] else False
		if self.xwindowsystem: 
			self.xwindowsystem = os.environ['DISPLAY'] # When the windowing system uses the DISPLAY enviromment variable, then KErL uses that same variable.
		self.processid = os.execve(self.argv[0], self.argv, self.env)
		self.settings_window = None # A Settings window.
		self.help_window = None # A Help window.
		self.main_window = window
		self.has_debug = False
		self.debug_window = None
	
	def run(self):
		''' Runs The Application. '''
		
		while self.should_run:
			print(f"(Event On Process {self.processid}) {self.currentEvent}")
			window.draw()