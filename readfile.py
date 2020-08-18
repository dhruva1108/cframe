import vaex
import dask.dataframe as dd
import modin.pandas as pd
import os

class Error(Exception):
    pass

class PathError(Error):
    pass

class FileTypeError(Error):
    pass

class Read:
    def __init__(self, a):
        self.a = a
    def check_path(self):
        if os.path.isfile(self.a) == False:
            raise PathError("Correct path of file should be given")
    def check_type(self):
        self.check_path()
        name, extension = os.path.splitext(self.a)
        if extension != '.csv':
            raise FileTypeError(".csv file should be given")
    def dframe(self):
        self.check_type()
        self.df_dask = dd.read_csv(self.a)
        return self.df_dask
    def pframe(self):
        self.dframe()
        self.df_pandas = self.df_dask.compute()
        return self.df_pandas
    def vframe(self):
        self.pframe()
        self.df_vaex = vaex.from_pandas(self.df_pandas)
        return self.df_vaex