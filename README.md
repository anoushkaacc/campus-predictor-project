# 🌟 Campus Placement Predictor

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-%20Framework-orange)](https://flask.palletsprojects.com/) [![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-brightgreen)](https://scikit-learn.org/stable/)

## 📹 Demo Video

https://drive.google.com/file/d/1yJ_aF1PUVMSHI-05CpRyfDy1DcBcYQv7/view?usp=sharing

---


An interactive web application designed to predict campus placement salaries for Computer Science students based on their academic and extracurricular profiles. This project uses machine learning models to provide insights and personalized recommendations for skill enhancement.

---

## ✨ Features

- **🎓 Salary Prediction**: Predict expected salaries based on various features like GPA, internships, and technical skills.
- **🛠️ Skill Recommendations**: Offers actionable advice to improve employability.
- **🌐 Web Interface**: Interactive and user-friendly interface powered by Flask.
- **📊 Machine Learning**: Employs a Random Forest Classifier for accurate predictions.

---

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Machine Learning**: Random Forest Classifier
- **Libraries**:
  - Scikit-learn
  - Pandas
  - NumPy
  - Pickle

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or later
- Required dependencies:
  ```bash
  pip install -r requirements.txt


Installation
Clone the repository:

```bash

git clone https://github.com/anoushkaacc/campus-predictor-project.git
cd campus-predictor-project
```
Run the Flask application:

```bash
python app.py
```
Open your browser and navigate to http://127.0.0.1:5000

---
## 🗂️ Project Structure

```plaintext
campus-predictor-project/
├── templates/
│   ├── home.html        # Input form for user data
│   ├── result.html      # Displays predicted salary and recommendations
├── static/
│   └── style.css        # Basic styling for the application
├── app.py               # Main Flask app
├── Salary_prediction.py # Model training and serialization
├── model1.pkl           # Pre-trained machine learning model
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

---


# ⚙️ How It Works
Input Features: The user inputs details such as GPA, gender, internships, and participation in hackathons. \
Data Processing: Encodes and preprocesses the input data using Scikit-learn. \
Model Prediction: Uses a trained Random Forest Classifier to predict the salary range. \
Recommendations: Displays personalized suggestions for skill development. 
