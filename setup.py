from setuptools import setup, find_packages


#with open('README.mk') as f:
#    readme = f.read()

setup(
    name='aavf',
    version='0.0.1',
    description='Aesthetic and Affective Visual Features',
    #long_description=readme,
    author='Daniel Morales Federico Matinelli',
    author_email='dnlmrls9@gmail.com',
    url='https://github.com/DanielMorales9/AAVF',
    #license=license,
    packages=find_packages(exclude=('docs'))
)