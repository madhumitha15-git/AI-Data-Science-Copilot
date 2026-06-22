import shap
import shap
import matplotlib.pyplot as plt



def explain_model(model, X_test):


    try:


        explainer = shap.TreeExplainer(
            model
        )


        shap_values = explainer.shap_values(

            X_test,

            check_additivity=False

        )



        fig = plt.figure()



        if isinstance(shap_values, list):

            shap_values = shap_values[1]



        shap.summary_plot(

            shap_values,

            X_test,

            show=False

        )


        return fig



    except Exception as e:


        fig = plt.figure()


        plt.text(

            0.1,

            0.5,

            "SHAP explanation not available"

        )


        return fig