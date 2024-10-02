import numpy as np

def drop_empty(df):
    return df.dropna(axis=0)

def fill_empty(df,col):
    return df.fillna(df[col].mean())

def drop_column(df,col):
    return df.drop(columns=[column_name])

def fix_index(df):
    return df.reset_index(drop=True)


def fix_dates(df):
    return pd.to_datetime(df[col])