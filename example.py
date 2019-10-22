from dependencies import Dependencies
try:
	import colorama
	import selenium
except ImportError:
	dependencies = Dependencies('colorama', 'selenium')
	dependencies.install_requirements()
	import colorama
	import selenium