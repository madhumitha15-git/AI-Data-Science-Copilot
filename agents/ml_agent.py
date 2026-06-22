import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (
    accuracy_score,
    r2_score
)

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression
)



def train_ml_models(df, target_column):


    report = {}


    # Split features and target

    X = df.drop(
        target_column,
        axis=1
    )


    y = df[target_column]



    # Encode categorical features

    categorical_cols = X.select_dtypes(
        include="object"
    ).columns


    encoder = LabelEncoder()


    for col in categorical_cols:

        X[col] = encoder.fit_transform(
            X[col]
        )



    # Encode target

    if y.dtype == "object":

        y = encoder.fit_transform(
            y
        )



    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42

    )



    # Detect problem type

    if len(set(y)) <= 10:


        problem = "Classification"


        models = {

            "Logistic Regression":
                LogisticRegression(max_iter=1000),


            "Random Forest":
                RandomForestClassifier(
                    random_state=42
                )

        }


    else:


        problem = "Regression"


        models = {


            "Linear Regression":
                LinearRegression(),


            "Random Forest":
                RandomForestRegressor(
                    random_state=42
                )

        }




    results = {}

    trained_models = {}



    # Train models

    for name, model in models.items():


        model.fit(

            X_train,

            y_train

        )


        predictions = model.predict(

            X_test

        )


        if problem == "Classification":


            score = accuracy_score(

                y_test,

                predictions

            )


        else:


            score = r2_score(

                y_test,

                predictions

            )


        results[name] = score


        trained_models[name] = model




    # Select best model

    best_model_name = max(

        results,

        key=results.get

    )


    final_model = trained_models[best_model_name]



    report["Problem Type"] = problem

    report["Model Scores"] = results

    report["Best Model"] = best_model_name

    report["Best Score"] = results[best_model_name]



    return report, final_model, X_test