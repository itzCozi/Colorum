from setuptools import setup, find_packages
import sys, os

VERSION = '0.1' 
DESCRIPTION = 'Colorum is a python package for changing the color of the console.'
LONG_DESCRIPTION = '''
A python package for coloring outputs in the console, more on github.
https://github.com/itzCozi/Colorum
'''

sys.path.append("C:/Users/" + os.getlogin() + "/scoop/apps/python/current/Lib/site-packages")

# Setting up
setup(
        name="Colorum", 
        version=VERSION,
        author="Cooper ransom",
        author_email="Cooperransom08@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['sys', 'os'], 
        
        keywords=['python', 'data', 'extraction', 'list'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)