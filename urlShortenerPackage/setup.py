from setuptools import setup

setup(
    name='url',
    version='1.0.4',
    description='SHORTENER TO REDUCE THE ENTERED LINK',
    url='https://github.com/abhijithwarrier',
    author='Abhijith Warrier',
    author_email='pythonscripts94@gmail.com',
    license='BSD 2-clause',
    packages=['url'],
    entry_points={
        'console_scripts': [
            'url=url.url:run',
        ],
    },
)