# TODO: Document this module.

import sys
import os
from KErL.kerl.buffer import *

cpdef class Font:
	''' A Font Object Used for displaying texto with custom fonts. '''
	
	def __init__(self, list filepaths):
		self.filepaths = filepaths
		self.files = [open(file, 'rb') for file in self.filepaths]
		self.main_font = None # No main font (yet!)
		self.buffer_arr = []
		self.buffer_arr.extend(self.files)

Font systemfont = None # No system font set. (yet!)

if sys.platform[3:] == 'darwin' or sys.platform == 'ios':
	systemfont = Font(os.listdir(os.path.join(os.path.dirname(__file__), "/fonts/mac/")))
	systemfont.main_font = open(os.path.join(os.path.dirname(__file__), "/fonts/mac/regular.otf"), 'rb')
else if sys.platform = 'win32':
	systemfont = Font(os.listdir(os.path.join(os.path.dirname(__file__), "/fonts/win32-msdos")))
	systemfont.main_font = open(os.path.join(os.path.dirname(__file__), "/fonts/win32-msdos/micross.otf")))
else: raise RuntimeError('Platform font is not supported.')
