from distutils.core import setup

setup(
	# Application name:
	name="gatewayutils",

	# Version number (initial):
	version="0.1.0",

	py_modules=[
		'dbutils',
		'decorators',
		'funcutils',
		'httputils',
		'messageutils',
		'parseutils',
		'pubsub',
		'queueutils'
	],

	# Application author details:
	author="Logi Leifsson",
	author_email="logileifs@gmail.com",

	# Packages
	#packages=["app"],

	# Include additional files into the package
	#include_package_data=True,

	# Details
	#url="http://pypi.python.org/pypi/MyApplication_v010/",

	#
	# license="LICENSE.txt",
	#description="Useful towel-related stuff.",

	# long_description=open("README.txt").read(),

	# Dependent packages (distributions)
	install_requires=[
		"redis",
		"disq",
	],
)