import pandas as pd


def analyze_dataset(df):

    info = {}

    info["rows"] = df.shape[0]
    info["columns"] = df.shape[1]

    info["missing_values"] = (
        df.isnull()
        .sum()
        .to_dict()
    )

    info["duplicates"] = (
        df.duplicated()
        .sum()
    )

    info["data_types"] = (
        df.dtypes
        .astype(str)
        .to_dict()
    )

    return info