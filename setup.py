import os
from setuptools import setup

__here__ = os.path.abspath(os.path.dirname(__file__))

package_name = 'ham'

# define __version__
# execfile doesn't exist in python 3
# see: http://stackoverflow.com/questions/6357361/alternative-to-execfile-in-python-3-2
exec(open(os.path.join(__here__, package_name, '_version.py')).read())


setup(
    name=package_name,
    description='Tools for syllable replacement',
    version=__version__,
    url='https://github.com/ftobia/ham',
    license='MIT license',
    author='Frank Tobia',
    install_requires=['nltk'],
    author_email='frank.tobia@gmail.com',
    packages=['ham'],
    include_package_data=True,
    #long_description='',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
)
