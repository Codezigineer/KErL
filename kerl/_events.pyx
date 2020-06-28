from threading cimport Event
import threading

cdef class Event(threading.Event):
     def __cinit__(self, basestring name):
        self.name = name

cdef class EventListener:
     def __cinit__(self):
        self.currentEvent = None
        cdef Event currentEvent
        self.otherEvents = []
        cdef list otherEvents
        
     cdef oneventadded(self, Event event):
        pass # You have to implement this.
        