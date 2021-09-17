# CUSTOM PACKAGE TO FIND THE MEANING OF THE ENTERED WORD 

# What is the purpose this package?
When the command is run by passing an input word, the meaning of the entered text is displayed as the output in the terminal

# Overview of this Package:
This package is built using mainly PyDictionary library of Python.

## PyDictionary Library:
PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words. It uses WordNet for getting meanings, Google for translations, and synonym.com for getting synonyms and antonyms. This module uses Python Requests, BeautifulSoup4 and goslate as dependencies

# Package Requirements:
For this package to work it requires PyDictionary package of Python. The PyDictionary package is mentioned in the required section of setup.py file included in this folder. So the PyDictionary package gets automatically installed while installing this package itself.

# Installation:
### Method 1:
1. pip install git+https://github.com/abhijithwarrier/AWPythonPackages.git#subdirectory=dictionaryPackage <br>
### Method 2:
1. To install this package, first clone the repository using the command: <b> git clone https://github.com/abhijithwarrier/AWPythonPackages.git </b>
2. Navigate to the dictionaryPackage folder: <b>cd dictionaryPackage/ </b>
3. Install the package by running the following command: <b> python setup.py install </b>

# Usage:
Run the command by passing keyword <b> dictionary </b> along with required parameter <br><br>
Required Parameter:
1. <b> -w or --word </b>: WORD OF WHICH THE MEANING IS TO BE SEARCHED