from .readfile import Read
import modin.pandas as pd

class sframe:
    def __init__(self, b):
        self.df = Read(b).pframe()
    def zfill(self, a, z):
        x = self.df.columns.get_loc(a)
        y = self.df[a]
        del self.df[a]
        self.df.insert(x, a, y.str.zfill(z))
        return self.df

