from setuptools import setup

setup(
    name='dictionary',
    version='1.0.1',
    description='DICTIONARY PACKAGE TO GET THE MEANING OF ENTERED WORD',
    url='https://github.com/abhijithwarrier',
    author='Abhijith Warrier',
    author_email='pythonscripts94@gmail.com',
    license='BSD 2-clause',
    packages=['dictionary'],
    install_requires=[
        'PyDictionary'
    ],
    entry_points={
        'console_scripts': [
            'dictionary=dictionary.dictionary:run',
        ],
    },
)