from kerl.mainloop import *
from kerl.internerrors import *
import sys
import os
class Application(MainLoop):
	''' An Application object representing an application. '''
	
	def __init__(self, window):
		if window is None:
			raise InternalError("No window specified.")
		super().__init__()
		self.argc = sys.argc
		self.argv = sys.argv
		self.env = os.environ
		self.processid = os.execve(self.argv[0], self.argv, self.env)
		
	def run(self):
		''' Runs The Application. '''
		
		while self.should_run:
			print(f"(Event On Process {self.processid}) {self.currentEvent}")
			window.draw()