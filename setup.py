from setuptools import setup
from Cython.Build import cythonize
import setuptools
import os

desc = open(os.path.join(os.path.dirname(__file__), 'README.md'))
def getfiles():
	status = os.system("nohup echo kerl/*.pxd")
	if status != 0:
		return
	else: 
		pass
	path = (os.getcwd() + "/nohup.out")
	file = open(path)
	result = _su(file.read())
	
	for string in result:
		if string.endswith(".pxd"):
			string.remove(".pxd")
			string.remove(" ")
	
	return result
files = getfiles()
def _su(string):
    start, end = 0, 0
       
    while start < len(string):
        if string[end] == string[end-start]:
            return string[start:end + 1]
            end += 1
               
            if end == len(string): 
                start += 1
                end = start
        else: 
            start += 1
            end = start 	

setup(
	name="kerl",
	version="0.0.1",
	author="j-pack",
	author_email="iamjojozm@icloud.com",
	description='A Basic Framework based off of Kivy, Still Using Cython.',
	long_description=desc.read(),
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.8, >=4.0',
	ext_modules = [cythonize([os.path.join(os.path.dirname(__file__), f'kerl/_{file}.pyx')]) for file in files]
)

desc.close()
