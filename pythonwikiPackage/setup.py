from setuptools import setup

setup(
    name='pywiki',
    version='1.0.1',
    description='OPENS WIKIPEDIA PAGE OF THE ENTERED TERM',
    url='https://github.com/abhijithwarrier',
    author='Abhijith Warrier',
    author_email='pythonscripts94@gmail.com',
    license='BSD 2-clause',
    packages=['pywiki'],
    install_requires=[
        'wikipedia',
    ],
    entry_points={
        'console_scripts': [
            'pywiki=pywiki.pywiki:run',
        ],
    },
)