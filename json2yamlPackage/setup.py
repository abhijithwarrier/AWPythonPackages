from setuptools import setup

setup(
    name='json2yaml',
    version='2.0.0',
    description='JSON TO YAML CONVERTER',
    url='https://github.com/abhijithwarrier',
    author='Abhijith Warrier',
    author_email='pythonscripts94@gmail.com',
    license='BSD 2-clause',
    packages=['json2yaml'],
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
        'pyaml'
    ],
    entry_points={
        'console_scripts': [
            'json2yaml=json2yaml.json2yaml:run',
        ],
    },
)