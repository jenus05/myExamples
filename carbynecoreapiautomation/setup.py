"""A setuptools based setup module."""

# Always prefer setuptools over distutils
from distutils.core import setup

setup(
    name='carbynecoreapiautomation',
    version='0.1qa',
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(include=['coreapi',]),
    #license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    # The project's main homepage.
    url='http://github.services.ooyala.net/cescamilla/core-api/',
    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',

     # What does your project relate to?
    keywords='CoreAPI Carbyne',
)