from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='WebUI',
    version='0.2.0',
    author='Nick Johnstone',
    author_email='ncwjohnstone@gmail.com',
    packages=['webui'],
    scripts=['examples/test_app.py'],
    url='https://github.com/Widdershin/WebUI/',
    license='MIT',
    description='WebUI lets you create first class desktop applications in Python with HTML/CSS',
    long_description=open('README.rst').read(),
    install_requires=required,
)
