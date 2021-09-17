from setuptools import setup

setup(
    name='dictionary',
    version='1.0.0',
    description='DICTIONARY PACKAGE TO GET THE MEANING OF ENTERED WORD',
    url='https://github.com/abhijithwarrier',
    author='Abhijith Warrier',
    author_email='pythonscripts94@gmail.com',
    license='BSD 2-clause',
    packages=['dictionary'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'PyDictionary'
    ],
    entry_points={
        'console_scripts': [
            'dictionary=dictionary.dictionary:run',
        ],
    },
)