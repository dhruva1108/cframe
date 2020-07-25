import vaex
import dask.dataframe as dd
import modin.pandas as pd

def vframe(a):
    df_dask = dd.read_csv(a)
    df_pandas = df_dask.compute()
    df_vaex = vaex.from_pandas(df_pandas)
    return df_vaex
