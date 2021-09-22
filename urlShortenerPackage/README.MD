# CUSTOM PACKAGE TO SHORTEN THE ENTERED LONG URL

# What is the purpose this package?
When the command is run by passing an input long url, the long url is shortened which is displayed as the output in the terminal

# Overview of this Package:
This package is built using mainly urllib library of Python which is used to make API CALLS to TinyURL.

## TinyURL
TinyURL is a URL Shortening Service. TinyURL has not officially released an API for Python.

# urllib Library
The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.

# Package Requirements:
For this package to work it requires urllib package of Python which is an in-built package.

# Installation:
### Method 1:
1. pip install git+https://github.com/abhijithwarrier/AWPythonPackages.git#subdirectory=urlShortenerPackage <br>
### Method 2:
1. To install this package, first clone the repository using the command: <b> git clone https://github.com/abhijithwarrier/urlShortenerPackage.git </b>
2. Navigate to the urlShortenerPackage folder: <b>cd urlShortenerPackage/ </b>
3. Install the package by running the following command: <b> python setup.py install </b>

# Usage:
Run the command by passing keyword <b> url </b> along with required parameter <br><br>
Required Parameter:
1. <b> -l or --link </b>: LONG URL WHICH IS TO BE SHORTENED