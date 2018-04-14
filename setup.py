from setuptools import setup

setup(
	name = 'basic-cli',
	version = '0.1.0',
	packages = ['basic_cli'],
	entry_points = {
		'console_scripts': [
			'basic-cli = basic_cli.__main__:main'
		]
	})