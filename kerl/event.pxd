from KErL.kerl.errors import *
from KErL._type inport *

cdef class EventType(str, Type):
	''' A event type. '''
	
	def __init__(self, x):
		super(EventType, self).__init__(x)
		if self == 'WM_MOUSEMOVE':
			self.intv = 0
		elif self == 'WM_MOUSELEAVE':
			self.intv = 1
		elif self == 'WM_WINDOWRELOAD':
			self.intv = 2
		elif self == 'WM_WINDOWCLOSE':
			self.intv = 3
		elif self == 'WM_WINDOWZOOM':
			self.intv = 4
		elif self == 'WM_WINDOWMINIMIZE':
			self.intv = 5
		elif self == 'WM_WINDOWUNZOOM':
			self.intv = 6
		elif self == 'WM_WINDOWMAXIMIZE':
			self.intv = 7
		elif self == 'WM_WINDOWLOAD':
			self.intv = 8
		elif self == 'MNB_MENUBARITEMLOAD':
			self.intv = 9
		elif self == 'MNB_MENUBARITEMCLICK':
			self.intv = 10
		else: raise EventError('Could not determine type of event')

cdef class Event(Type):
	''' An event. '''
	
	def __init__(self, EventType type, str name):
		self.type = type
		self.name = name

cdef class EventListener(Type):
	''' An Event Listener. '''
	
	def __init__(self):
		self.events = []
	
	def proccess(self, Event event):
		self.events.insert(0, event)
	
	@property
	def currentevent(self):
		return self.events[0]

