from setuptools import setup, find_packages
import os

#cwd_name=os.path.basename(os.getcwd())

setup(
	name='pycli',
	version='1.0.0',
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			'pycli=pycli.__main__:main'
		]
	})
