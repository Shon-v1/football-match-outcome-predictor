# ⚽ Premier League Match Outcome Predictor

A Machine Learning-powered web application that predicts **Premier League football match outcomes** (Home Win / Draw / Away Win) using historical match data and team performance metrics.

## 🚀 Project Overview

This project uses **Machine Learning (XGBoost Classifier)** to predict football match results based on:

- Team Form (Last 5 Matches)
- Average Goals Scored
- Average Goals Conceded
- Matchday Information
- Referee Data
- Home & Away Team Statistics

The model is integrated into an **interactive Streamlit web application**, allowing users to enter match details and receive predictions instantly.

---

## 🎯 Features

✅ Predict Home Win / Draw / Away Win  
✅ Interactive Streamlit Web Interface  
✅ Team Form-Based Feature Engineering  
✅ XGBoost Machine Learning Model  
✅ Real-Time Match Prediction  
✅ Premier League Team Selection

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-Learn**
- **XGBoost**
- **Joblib**
- **Streamlit**

---

## 📊 Machine Learning Workflow

### 1. Data Preprocessing
- Cleaned football match dataset
- Removed unnecessary columns
- Encoded categorical features
- Handled missing values

### 2. Feature Engineering
Created additional features such as:

- Home Team Form
- Away Team Form
- Average Goals Scored
- Average Goals Conceded

### 3. Model Training
Used **XGBoost Classifier** for match outcome prediction.

### 4. Model Deployment
Built an interactive **Streamlit web application** for predictions.

---

## 📂 Project Structure

```text
Football Match Outcome Predictor
│── app.py
│── requirements.txt
│── README.md
│
├── model
│   ├── xgboost_model.pkl
│   ├── label_encoders.pkl
│   └── target_encoder.pkl
│
├── notebook
│   └── Football_Prediction.ipynb
│
├── images
│   ├── football1.jpg
│   ├── football2.jpg
│   └── football3.jpg
│
├── screenshots
│   └── app_screenshot.png
│
└── data
    └── footballmatches-2024-2025.csv
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/football-match-outcome-predictor.git
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📸 Application Preview

![App Screenshot](screenshots/app_screenshot1.png)

---

## 📈 Model Performance

Current model accuracy:

**~48% Accuracy**

Football prediction is inherently difficult due to the unpredictable nature of sports, injuries, tactics, and real-world match dynamics.

---

## 🔮 Future Improvements

- Add Multiple League Support
- Improve Prediction Accuracy
- Live Match Statistics API
- Team Performance Visualization
- Enhanced UI/UX

---

## 👨‍💻 Author

**Shon Varghese**  
Aspiring Data Analyst | Machine Learning Enthusiast | Python Developer

GitHub: https://github.com/Shon-v1

---

⭐ If you like this project, consider giving it a star!