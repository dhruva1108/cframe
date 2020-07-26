# cframe
### This is a python package designed to read Big_Data and do the operations. It involves libraries dask, vaex, modin.pandas, numpy and matplotlib. All this libraries are imported in "__init__.py" file.
### Importing the library - 
#### from cframe import *
### Getting a vaex dataframe - 
#### df = vframe(Filename in csv)
### Getting a dask dataframe - 
#### df = dframe(Filename in csv)
### Getting a pandas dataframe - 
#### df = pframe(Filename in csv)
### Code for libraries
#### dask as dask
#### vaex as vaex
#### modin.pandas as pd
#### numpy as np
#### matplotib as mlt
### Note: You do need to import the above libraries again since they are already imported in the "__init__.py" file unless you want to import a particular sub-package from them
