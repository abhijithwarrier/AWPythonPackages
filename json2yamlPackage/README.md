# CUSTOM PACKAGE TO CONVERT JSON FILE TO YAML FILE & YAML FILE TO JSON FILE

# What is a JSON FILE?
A JSON file is a file that stores simple data structures and objects in JavaScript Object Notation (JSON) format, which is a standard data interchange format. It is primarily used for transmitting data between a web application and a server. JSON files are lightweight, text-based, human-readable, and can be edited using a text editor.
json module has a built-in package called json. This json module can be used to work with JSON data.

# What is a YAML FILE?
YAML is a human-readable data serialization standard that can be used in conjunction with all programming languages and is often used to write configuration files. 
The recursive YAML acroynym stands for “YAML Ain’t Markup Language,” denoting it as flexible and data-oriented. In fact, it can be used with nearly any application that needs to store or transmit data. Its flexibility is partially due to the fact that YAML is made up of bits and pieces of other languages

# Overview of this Package:
This package is built using mainly json and PyYAML libraries of Python.

## json Library
Python has a built-in package called json , which can be used to work with JSON data. The json library can parse JSON from strings or files. The library parses JSON into a Python dictionary or list. It can also convert Python dictionaries or lists into JSON strings.

## PyYAML Library
PyYAML is a YAML parser and emitter for Python. PyYAML features a complete YAML 1.1 parser, Unicode support, pickle support, capable extension API, and sensible error messages. PyYAML supports standard YAML tags and provides Python-specific tags that allow to represent an arbitrary Python object. PyYAML is applicable for broad range of tasks from complex configuration files to object serialization & persistence.

# Package Requirements:
For this package to work it requires PyYAML package of Python. The PyYAML package is mentioned in the required section of setup.py file included in this folder. So the PyYAML package gets automatically installed while installing this package itself.

# Installation:
### Method 1:
1. pip install git+https://github.com/abhijithwarrier/AWPythonPackages.git#subdirectory=json2yamlPackage <br>
### Method 2:
1. To install this package, first clone the repository using the command: <b> git clone https://github.com/abhijithwarrier/PythonPackages.git </b>
2. Navigate to the json2yamlPackage folder: <b>cd json2yamlPackage/ </b>
3. Install the package by running the following command: <b> python setup.py install </b>

# Usage:
Run the command by passing keyword <b> json2yaml </b> along with required parameters<br><br>
Required Parameters:
1. <b> -j or --json </b>: JSON FILE NAME ALONG WITH PATH
2. <b> -y or --yaml </b>: YAML FILE NAME ALONG WITH PATH
3. <b> -m or --mode </b>: CONVERSION MODE (JSON TO YAML OR YAML TO JSON)<br>
   a. VALUE TO BE PASSED FOR JSON TO YAML CONVERSION : <b> j2y or json2yaml </b><br>
   b. VALUE TO BE PASSED FOR YAML TO JSON CONVERSION : <b> y2j or yaml2json </b>