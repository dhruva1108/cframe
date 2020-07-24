# cframe
# This is a package which has been developed to read large csv files at a faster rate.
# It involves libraries dask, vaex and modin.pandas
# This returns a vaex dataframe and you can use all the operations for a dataframe which are on vaex. Studies show that vaex does the calculations faster.
# Process to import:
from cframe import cframe
df = cframe.cframe(your csv file name in quotes)
# now this df will be a vaex dataframe so you can import vaex and do the required operations and manipulations
