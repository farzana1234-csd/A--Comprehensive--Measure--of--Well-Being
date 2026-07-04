# HDI Prediction System 🌍📊

### Predicting the Human Development Index using Machine Learning

---

## 📖 About the Project

The **Human Development Index (HDI)** is a summary measure used by the United Nations to assess a country's overall achievement in three key dimensions of human development: **a long and healthy life, access to knowledge, and a decent standard of living.**

Traditionally, calculating HDI requires collecting and combining multiple statistics manually. This project simplifies that process by using a **Machine Learning model** that can instantly predict a country's HDI score just by taking a few key socio-economic indicators as input.

The goal of this project is to build an end-to-end system — from data collection and model training to a fully functional, deployed web application — that allows anyone to estimate a country's HDI in real time.

---

## ❓ Problem Statement

Government bodies, researchers, and policy makers often need quick estimates of a region's development level without waiting for official HDI reports, which are published only once a year and can be delayed. There was a need for a **fast, accessible, and data-driven tool** that could estimate HDI using easily available indicators — helping in preliminary analysis, awareness, and educational purposes.

---

## 💡 Proposed Solution

We built a **Linear Regression–based prediction system** trained on real-world 2021 global HDI data covering **~195 countries**. The model learns the relationship between HDI and four core indicators:

1. **Life Expectancy** – average lifespan of a country's population
2. **Expected Years of Schooling** – years a child is expected to spend in education
3. **Mean Years of Schooling** – average education years of adults
4. **GNI per Capita** – Gross National Income per person, reflecting standard of living

Once trained, the model was wrapped inside a **Flask web application** so users can simply enter these four values and instantly get a predicted HDI score.

---

## 🔍 How It Works

1. **Data Collection** – Global HDI dataset (2021) sourced and cleaned for training.
2. **Model Training** – A Linear Regression model was trained on the four features using scikit-learn, achieving a strong **R² score of ~0.98**, meaning the model explains 98% of the variation in HDI scores.
3. **Model Serialization** – The trained model was saved as `hdi_model.pkl` for reuse without retraining.
4. **Web Application** – A Flask backend loads the model and serves a simple, dark-themed interface where users input the four indicators.
5. **Prediction** – On submission, the backend processes the inputs, runs them through the model, and displays the predicted HDI score instantly on the same page.
6. **Deployment** – The complete application was deployed on **Render**, making it publicly accessible without any local setup.

---

## 📊 Results

| Metric | Value |
|---|---|
| Model Used | Linear Regression |
| Dataset Size | ~195 countries (2021 data) |
| R² Score | ~0.98 |
| Features Used | 4 (Life Expectancy, Schooling x2, GNI per Capita) |

The high R² score confirms that HDI can be very accurately estimated using just these four indicators, validating the strong real-world correlation between health, education, and income with overall human development.

---

## 🎯 Use Cases

- Quick HDI estimation for academic or research purposes
- Educational tool to understand factors driving human development
- Awareness tool for students learning about global development indices
- Demonstration of applying ML to real-world socio-economic data

---

## 🛠️ Tech Stack

- **Machine Learning:** Python, scikit-learn, pandas, numpy
- **Web Framework:** Flask
- **Frontend:** HTML, CSS (custom dark theme)
- **Deployment:** Render
- **Version Control:** Git & GitHub

---

## 🔗 Links

- **Live Application:** [Deployed on Render](#) <!-- paste your Render URL here -->
- **GitHub Repository:** [github.com/farzana1234-csd/HDI-Prediction-System](https://github.com/farzana1234-csd/HDI-Prediction-System)

---

## 👩‍💻 Team & Acknowledgements

This project was completed as part of the **SmartBridge AI/ML Internship Program**, developed by a 5-member team with **Farzana** as **Team Lead**.

Special thanks to:
- SmartBridge AI/ML Internship Program
- NRI Institute of Technology, Guntur
- UNDP Human Development Reports (data source)

---

## 🚀 Future Scope

- Incorporating more features (e.g., environmental sustainability index, gender inequality index) for richer predictions
- Extending the model to advanced algorithms (Random Forest, XGBoost) for comparison
- Adding historical trend visualization for each country
- Building an API endpoint for third-party integrations
