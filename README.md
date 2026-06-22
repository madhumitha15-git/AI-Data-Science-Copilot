# 🤖 AI Data Science Copilot

An AI-powered Data Science assistant that helps users analyze datasets, generate insights, understand patterns, and automate data analysis workflows using Generative AI and Large Language Models.

The application combines Data Science techniques with LLM capabilities to provide intelligent analysis, explanations, and recommendations from uploaded datasets.

---

## 🚀 Features

- 📂 Upload CSV datasets
- 🔍 Automated Exploratory Data Analysis (EDA)
- 📊 Data visualization and statistical analysis
- 🤖 AI-generated business insights
- 🧠 Machine learning model explanation
- 💡 Natural language interaction with datasets
- ⚡ LLM-powered data analysis assistant
- 🐳 Docker support for deployment

---

## 🏗️ Project Architecture

```
User
 |
 | Upload Dataset
 |
Streamlit Interface
 |
Data Processing Layer
 |
EDA + ML Analysis
 |
LLM Integration (Groq)
 |
AI Generated Insights
 |
User Output
```

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Data Science
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- XGBoost
- SHAP

### Generative AI
- LangChain
- LangGraph
- Groq LLM

### Application
- Streamlit

### Deployment
- Docker

---

## 📁 Project Structure

```
AI_Data-_Science_Copilot
│
├── app.py
│
├── llms
│   └── llm_connect.py
│
├── requirements.txt
│
├── Dockerfile
│
├── .dockerignore
│
├── README.md
│
└── screenshots
    └── app.png
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/madhumitha15-git/AI_Data-_Science_Copilot.git
```

Navigate into project:

```bash
cd AI_Data-_Science_Copilot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

The API key is loaded securely using environment variables.

---

# ▶️ Run Application Locally

Start Streamlit:

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 🐳 Run Using Docker

## Build Docker Image

```bash
docker build -t ai-data-science-copilot .
```

---

## Run Container

```bash
docker run --env-file .env -p 8501:8501 ai-data-science-copilot
```

Open:

```
http://localhost:8501
```

---

# 📸 Screenshots

Add application screenshots here:

```
screenshots/app.png
```

Example:

![AI Data Science Copilot](screenshots/app.png)

---

# 🔮 Future Improvements

- Add support for multiple file formats
- Add advanced ML model training pipeline
- Add automated model selection
- Add database connectivity
- Deploy using cloud infrastructure
- Add user authentication

---

# 👨‍💻 Author

**Madhumitha**

B.Tech Student | Data Science | Generative AI | Machine Learning

---

# ⭐ Acknowledgements

Built using modern AI technologies to simplify data analysis and make Data Science workflows more accessible.