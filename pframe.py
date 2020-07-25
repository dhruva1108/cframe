import dask.dataframe as dd
import modin.pandas as pd

def pframe(a):
    df_dask = dd.read_csv(a)
    df_pandas = df_dask.compute()
    return df_pandas
