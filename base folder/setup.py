from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Topsis package'


# Setting up
setup(
    name="topsis-Piyush-102003417",
    version=VERSION,
    author="Piyush Sharma",
    author_email="<piyush56.ps17@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    keywords=['python', 'topsis', 'machinelearning', 'datascience'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)