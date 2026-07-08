                                                📊 Customer Churn Prediction System

This project predicts whether a telecom customer is likely to churn using Machine Learning.

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

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Docker
- Git
- GitHub


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

![Home](images/home.png)

### Prediction Result

![Prediction](images/prediction.png)


## Future Improvements

- Improve prediction accuracy
- Add feature importance visualization
- Deploy using cloud services
- Add user authentication


## Author

Umera

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
