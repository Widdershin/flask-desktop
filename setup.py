from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="WebUI",
    version="0.2.1",
    author="Nick Johnstone",
    author_email="ncwjohnstone@gmail.com",
    packages=["webui"],
    scripts=["examples/test_app.py"],
    url="https://github.com/Widdershin/WebUI/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    description=(
        "WebUI lets you create first class desktop applications in Python with HTML/CSS"
    ),
    long_description=open("README.md").read(),
    install_requires=required,
    python_requires=">=3.6",
)
