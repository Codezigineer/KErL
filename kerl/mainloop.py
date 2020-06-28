from kerl.events import *

class MainLoop(EventListener):
	''' A MainLoop that can execute code continously. '''
	
	def __init__(self, code_to_execute=None):
		super().__init__()
		self.code_to_execute = code_to_execute
		self.should_run = true
	
	def run(self, i=-1):
		if i == -1: # This means it goes by the `should_run` property.
			while self.should_run:
				self.code_to_execute()
		else: # This means it goes by how mush seconds specified.
			msecs = i * 1000 # How much miliseconds.
			ii = 0
			while i < msecs:
				self.code_to_execute()

