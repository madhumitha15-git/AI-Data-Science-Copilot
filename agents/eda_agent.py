import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def generate_eda(df):

    plots = {}


    # Numeric columns

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns


    for col in numeric_cols:

        fig, ax = plt.subplots()

        sns.histplot(
            df[col],
            kde=True,
            ax=ax
        )

        ax.set_title(
            f"Distribution of {col}"
        )


        plots[f"{col}_distribution"] = fig



    # Correlation heatmap

    if len(numeric_cols) > 1:

        fig, ax = plt.subplots()

        sns.heatmap(
            df[numeric_cols].corr(),
            annot=True,
            ax=ax
        )

        ax.set_title(
            "Correlation Heatmap"
        )


        plots["correlation"] = fig



    return plots