from setuptools import setup, find_packages

VERSION = '0.5.1' 
DESCRIPTION = 'Colorum is a python package for changing the color of the console.'
LONG_DESCRIPTION = '''
A python package for coloring outputs in the console, more on github.
https://github.com/itzCozi/Colorum
'''

# Setting up
setup(
        name="Colorum", 
        version=VERSION,
        author="Cooper ransom",
        author_email="Cooperransom08@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'data', 'extraction', 'list'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)