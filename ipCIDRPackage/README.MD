# CUSTOM PACKAGE FOR IPv4 CIDR CALCULATOR

# What is the purpose this package?
When the command is run by passing an IPv4 Address, the CIDR (Classless Inter-Domain Routing) of the IP is calculated.

# Overview of this Package:
This package is built using ipaddress library of Python.

## ipaddress Library:
ipaddress provides the capabilities to create, manipulate and operate on IPv4 and IPv6 addresses and networks. Python’s ipaddress module is an underappreciated gem from the Python standard library. The functions and classes in this module make it straightforward to handle various tasks related to IP addresses, including checking whether two hosts are on the same subnet, iterating over all hosts in a particular subnet, checking whether a string represents a valid IP address or network definition, and so on.

# Installation:
### Method 1:
1. pip install git+https://github.com/abhijithwarrier/AWPythonPackages.git#subdirectory=ipCIDRPackage <br>
### Method 2:
1. To install this package, first clone the repository using the command: <b> git clone https://github.com/abhijithwarrier/AWPythonPackages.git </b>
2. Navigate to the ipCIDRPackage folder: <b>cd ipCIDRPackage/ </b>
3. Install the package by running the following command: <b> python setup.py install </b>

# Usage:
Run the command by passing keyword <b> pycidr </b> along with required parameter <br><br>
Required Parameter:
1. <b> -a or --address </b>: IPv4 ADDRESS