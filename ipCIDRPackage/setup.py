from setuptools import setup

setup(
    name='pycidr',
    version='1.0.0',
    description='IPv4 CIDR CALCULATOR',
    url='https://github.com/abhijithwarrier',
    author='Abhijith Warrier',
    author_email='pythonscripts94@gmail.com',
    license='BSD 2-clause',
    packages=['pycidr'],
    entry_points={
        'console_scripts': [
            'pycidr=pycidr.pycidr:run',
        ],
    },
)