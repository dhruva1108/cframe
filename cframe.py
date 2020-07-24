import dask.dataframe as dd
import modin.pandas
import vaex

def cframe(a):
    df_dask = dd.read_csv(a)
    df = df_dask.compute()
    df_vaex = vaex.from_pandas(df)
    return df_vaex
