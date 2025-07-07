# 📊 Customer Churn Prediction - Data Preprocessing

This project focuses on **preprocessing customer churn data** to prepare it for machine learning models. It includes data cleaning, categorical encoding, feature scaling, and train-test splitting — essential steps in any ML pipeline.

---

## 📽️ Demo

[▶️ Watch Demo on YouTube](https://youtu.be/RZk1biP-kSY)

---


Uploading demo.mp4…


## 📁 Project Structure

Level_1_Task_1/
│
├── preprocess.py # Python script for preprocessing
├── churn-bigml-80.csv # Raw dataset (local only, not pushed)
├── venv/ # Python virtual environment
├── demo.mp4 # Video demonstration of the project
├── README.md # Project documentation
├── .gitignore # Git ignored files list

---

## 🎯 Project Objectives

- ✅ Handle missing values (mean imputation)
- ✅ Encode categorical variables
  - Label Encoding for binary categories
  - One-Hot Encoding for multi-class categories
- ✅ Normalize numerical features using `StandardScaler`
- ✅ Split dataset into training and testing sets (80/20 split)

---

## 🧪 Tools & Technologies

- Python 🐍
- Pandas
- Scikit-learn
- GitHub

---

## 📊 Dataset Description

The dataset contains telecom customer usage data with features such as:

- `State` – customer’s state of residence
- `Account length`
- `Area code`
- `International plan` – Yes/No
- `Voice mail plan` – Yes/No
- `Total day/evening/night minutes & charges`
- `Customer service calls`
- `Churn` – target variable (TRUE/FALSE)

---

## ⚙️ Preprocessing Workflow

1. **Load the CSV dataset** with pandas
2. **Handle missing values** (fill with column mean or median)
3. **Label encode** binary categorical columns:
   - `international plan`
   - `voice mail plan`
   - `churn`
4. **One-hot encode** multi-class column:
   - `state`
5. **Standardize** all numerical features using `StandardScaler`
6. **Split** the dataset into training and test sets using `train_test_split`

---

## ▶️ How to Run the Project

```bash
# Clone the repo
git clone https://github.com/Kiranwaqar/DataPreprocessingforML.git
cd Level_1_Task_1

# Activate your virtual environment (optional)
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt  

# Run preprocessing script
python preprocess.py

---

## 🙋‍♀️ Author
Kiran Waqar
Second-Year Software Engineering Student
Passionate about Machine Learning and AI

---

## 🏁 Future Ideas
Apply ML models (Logistic Regression, Decision Tree, etc.)

Evaluate performance using accuracy, precision, recall

Deploy the model using Flask/Streamlit

Add user input features for predictions

