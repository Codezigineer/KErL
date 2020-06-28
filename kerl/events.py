try:
	import kerl._events
except ImportError:
	raise ModuleError("You did not install KErL correctly.")

EventListener = _events.EventListener
Event = _events.Event