# TODO: Document this module.

from kerl.widget import *
from kerl.canvas import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Window(Widget):
	''' A Window. '''
	
	def __init__(self, canvas=Canvas, windowname="Window", parent=None):
		super().__init__(canvas=canvas, parent=parent)
		self.windowname = windowname
		glBegin()
		if glutInit: 
			glutInit()
		glutInitDisplayMode(GLUT_RGBA)
		glutInitWindowSize(self.canvas.width, self.canvas.height)
		glutInitWindowPosition(self.canvas.x, self.canvas.y)
		self._window = glutInitWindow((self.windowname)
		glutDisplayFunc(self.draw)
		glutIdleFunc(self.draw)
		glutMainLoop()

	def draw():
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glutSwapBuffers()
