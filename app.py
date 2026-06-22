import streamlit as st
import pandas as pd


# Agents

from utils.preprocessing import analyze_dataset

from agents.data_cleaning_agent import clean_dataset

from agents.eda_agent import generate_eda

from agents.ml_agent import train_ml_models

from agents.explain_agent import explain_model


# LLM

from llms.llm_connect import generate_insight



# Page Config

st.set_page_config(
    page_title="AI Data Scientist Copilot",
    layout="wide"
)



st.title("🤖 AI Data Scientist Copilot")

st.write(
    "Automated EDA, Machine Learning, Explainable AI and AI Insights"
)



# Upload Dataset

file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)



if file is not None:



    # ==========================
    # Load Dataset
    # ==========================

    df = pd.read_csv(file)



    st.subheader(
        "📌 Dataset Preview"
    )


    st.dataframe(
        df.head()
    )




    # ==========================
    # Dataset Analysis
    # ==========================

    st.subheader(
        "📊 Dataset Analysis"
    )


    analysis = analyze_dataset(df)


    st.json(
        analysis
    )




    # ==========================
    # Cleaning Agent
    # ==========================

    st.subheader(
        "🧹 Data Cleaning Agent"
    )


    cleaned_df, cleaning_report = clean_dataset(df)



    st.write(
        "Cleaning Report"
    )


    st.json(
        cleaning_report
    )


    st.write(
        "Cleaned Dataset"
    )


    st.dataframe(
        cleaned_df.head()
    )





    # ==========================
    # EDA Agent
    # ==========================

    st.subheader(
        "📈 Exploratory Data Analysis"
    )


    eda_results = generate_eda(
        cleaned_df
    )



    for name, plot in eda_results.items():


        st.write(
            name
        )


        st.pyplot(
            plot
        )





    # ==========================
    # ML Agent
    # ==========================


    st.subheader(
        "🤖 Machine Learning Agent"
    )



    target_column = st.selectbox(

        "Select Target Column",

        cleaned_df.columns

    )



    if st.button("Train ML Models"):



        ml_report, model, X_test = train_ml_models(

            cleaned_df,

            target_column

        )



        st.subheader(
            "Model Performance"
        )


        st.json(
            ml_report
        )





        # ==========================
        # SHAP
        # ==========================


        st.subheader(
            "🔍 Explainable AI - SHAP"
        )



        shap_plot = explain_model(

            model,

            X_test

        )



        st.pyplot(
            shap_plot
        )






        # ==========================
        # LLM INSIGHTS
        # ==========================


        st.subheader(
            "🧠 AI Generated Data Science Insights"
        )



        try:


            insight = generate_insight(

                ml_report

            )


            st.write(
                insight
            )


        except Exception as e:


            st.error(
                f"LLM Error: {e}"
            )





else:


    st.info(
        "Upload a CSV dataset to start analysis."
    )