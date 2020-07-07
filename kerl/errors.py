from kerl.log import *

class KErLError: 
	''' Base class for KErL errors. '''
	
	def __init__(self, msg):
		self.msg = msg
		log.error(self.msg)
		exit(1)

class InternalError(KErLError):
	''' Raised when a internal error happens. '''
	
	def __init__(self, **kw):
		self.msg = kw['msg']
		self.errno = kw['errno']
		if self.msg:
			log.error(f'[Errno. {self.errno}] {self.msg}') if self.errno else log.error(self.msg)

class EventError(InternalError): pass