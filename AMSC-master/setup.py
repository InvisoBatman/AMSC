from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests', 're', 'time', ]

# some more details
CLASSIFIERS = [
    'Development Status :: initial Beta',
    'Intended Audience :: My grandparents',
    'Topic :: survey',
    'License :: OSI Approved :: none',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.10.4',
    ]

# calling the setup function 
setup(name="Auto-McDonald's-Survey-Completer",
      version='1.0.0',
      description="A program that expedites the McDonald's survey proccess",
      long_description=long_description,
      url='',
      author='Ian Blake Lawson',
      author_email='ian.lawson42@gmail.com',
      license='',
      packages=[],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords="McDonald's survey fastfood fast food"
      )
