from setuptools import setup, find_packages
import sys, os

with open('README.rst') as f:
    readme = f.read()

sys.path.insert(0, os.path.abspath('/usr/local/lib/python2.7/site-packages'))

setup(
    name='aavf',
    version='0.0.1',
    description='Aesthetic and Affective Visual Features',
    long_description=readme,
    author='Daniel Morales Federico Matinelli',
    author_email='dnlmrls9@gmail.com',
    url='https://github.com/DanielMorales9/AAVF',
    #license=license,
    packages=find_packages(exclude=('docs')),
    test_suite='nose.collector',
    tests_require=['nose'], install_requires=['numpy']
)