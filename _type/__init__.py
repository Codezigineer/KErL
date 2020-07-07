class TypeMeta(type):
	pass

class Type(object, metaclass=TypeMeta):
	def __init__(self):
		super().__init__()
