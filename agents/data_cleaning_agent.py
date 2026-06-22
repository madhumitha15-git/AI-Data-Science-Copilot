import pandas as pd
import numpy as np


def clean_dataset(df):

    report = {}

    # Original shape
    report["original_shape"] = df.shape


    # Missing values before
    missing_before = df.isnull().sum().sum()

    report["missing_values_before"] = int(missing_before)


    # Handle missing values
    for col in df.columns:

        if df[col].isnull().sum() > 0:

            if df[col].dtype == "object":

                df[col].fillna(
                    df[col].mode()[0],
                    inplace=True
                )

            else:

                df[col].fillna(
                    df[col].median(),
                    inplace=True
                )


    missing_after = df.isnull().sum().sum()

    report["missing_values_after"] = int(missing_after)



    # Remove duplicates

    duplicates = df.duplicated().sum()

    report["duplicates_removed"] = int(duplicates)

    df.drop_duplicates(
        inplace=True
    )



    # Outlier detection

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns


    outlier_report = {}


    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)

        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1


        outliers = df[
            (df[col] < Q1 - 1.5*IQR) |
            (df[col] > Q3 + 1.5*IQR)
        ]


        outlier_report[col] = len(outliers)


    report["outliers"] = outlier_report



    report["final_shape"] = df.shape


    return df, report