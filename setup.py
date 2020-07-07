from setuptools import setup
from Cython.Build import cythonize
import setuptools
import os

desc = open(os.path.join(os.path.dirname(__file__), 'README.md'))
files = ["canvas", "event", "color", "pixel"]
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
	ext_modules = cythonize([os.path.join(os.path.dirname(__file__), f'kerl/_{file}.pyx'] for file in files)
)

desc.close()