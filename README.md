                                                  📊 Customer Churn Prediction System
                                                
A Machine Learning web application that predicts whether a telecom customer is likely to churn based on customer demographics, account information, and subscribed services.
This project predicts whether a telecom customer is likely to churn using Machine Learning.


## 🌐 Live Demo

Streamlit App:
https://customerchurnprediction-kgrg.onrender.com



The project includes:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Model training and evaluation
- Streamlit web application
- Docker support for deployment

## Features

- Predict customer churn
- Interactive Streamlit web app
- Machine Learning model
- Docker support
- GitHub version control
- Easy to deploy

## Project Structure

```text
customerchurnprediction/
│
├── app/
├── data/
├── images/
├── models/
├── notebooks/
├── reports/
├── src/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Dataset

IBM Telco Customer Churn Dataset

The dataset contains customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Internet Service
- Contract Type
- Monthly Charges
- Total Charges

Target Variable:

- Churn (Yes / No)
- After filling in the details, users can click Predict Churn to receive the prediction.

## 🛠️ Technologies Used

- Python
- Streamlit
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- MLflow
- Docker
- Render
- Git & GitHub



## 🤖 Machine Learning Model

**Algorithm**

- Logistic Regression!


### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score


## Installation

Clone the repository

```bash
git clone https://github.com/umera333/customerchurnprediction.git
```

Go to project folder

```bash
cd customerchurnprediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app/streamlit_app.py
```

## Run with Docker

Build Docker Image

```bash
docker build -t customer-churn-app .
```

Run Container

```bash
docker run -p 8501:8501 customer-churn-app
```

## Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/0a4747b6-9066-4754-a0bf-ad2287e6b80e)




### Prediction Result

![Prediction Result](https://github.com/user-attachments/assets/681f671c-5bda-41e3-88c1-75c514a4d221)




### 📊 MLflow Dashboard

![MLflow Dashboard](https://github.com/user-attachments/assets/d8984fcb-c8dd-4eed-b0d5-c93728bf0476)




### ⚡ FastAPI Swagger Documentation

![Swagger API](https://github.com/user-attachments/assets/214b5ae7-d713-4037-8f9f-404d07209f3b)



## Future Improvements

- Improve prediction accuracy
- Add feature importance visualization
- Deploy using cloud services
- Add user authentication


## Author

Umera Khwaja

GitHub:
https://github.com/umera333




📊 Customer Churn Prediction System

About
Features
Project Structure
Dataset
Technologies
Installation
Docker
Screenshots
Future Improvements
Author
