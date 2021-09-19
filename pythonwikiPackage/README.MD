# CUSTOM PACKAGE TO OPEN WIKIPEDIA PAGE IN THE BROWSER ABOUT THE ENTERED INPUT

# What is the purpose this package?
When the command is run by passing an input, the wikipedia page of the entered input is opened in a new browser tab.

# Overview of this Package:
This package is built using wikipedia and webbrowser libraries of Python.

## wikipedia Library:
Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia. Wikipedia API is used to retrieve data from Wikipedia

# Package Requirements:
For this package to work it requires wikipedia package of Python. The wikipedia package is mentioned in the required section of setup.py file included in this folder. So the wikipedia package gets automatically installed while installing this package itself.

# Installation:
### Method 1:
1. pip install git+https://github.com/abhijithwarrier/AWPythonPackages.git#subdirectory=pythonwikiPackage <br>
### Method 2:
1. To install this package, first clone the repository using the command: <b> git clone https://github.com/abhijithwarrier/AWPythonPackages.git </b>
2. Navigate to the pythonwikiPackage folder: <b>cd pythonwikiPackage/ </b>
3. Install the package by running the following command: <b> python setup.py install </b>

# Usage:
Run the command by passing keyword <b> pywiki </b> along with required parameter <br><br>
Required Parameter:
1. <b> -i or --input </b>: INPUT OF WHICH WIKIPEDIA PAGE IS TO BE OPENED