from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
	name='WebUI',
	version='0.1.0',
	author='Nick Johnstone',
	author_email='ncwjohnstone@gmail.com',
	scripts=['examples/test_app.py'],
	url='http://pypi.python.org/pypi/WebUI/',
	license='LICENSE',
	description='WebUI lets you create first class desktop applications in Python with HTML/CSS',
	long_description=open('readme.md').read(),
	install_requires=required,
	py_modules=['foo'],
	)