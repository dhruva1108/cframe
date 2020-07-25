import dask.dataframe as dd

def dframe(a):
    df_dask = dd.read_csv(a)
    return df_dask
