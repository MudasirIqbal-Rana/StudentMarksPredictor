# Student Marks Predictor
📘 Student Marks Predictor (Machine Learning + Tkinter GUI)

This project predicts a student's expected marks based on their daily study hours using a Linear Regression Machine Learning model.
A simple and interactive Tkinter GUI is also included, where the user enters their name and study hours, and the app predicts their marks.

📂 Project Overview

This project includes:
✔ Machine Learning Model (Python)

Reads dataset student_info.csv

Cleans missing values

Splits data into training & testing sets

Trains a Linear Regression model

Saves the trained model as .pkl file

Visualizes study hours vs student marks

✔ GUI Application (Tkinter)

User enters name

User enters study hours

Displays predicted marks (with percentage format)

Includes image banner using PIL (Pillow)

Uses the trained model (student_marks_predictor.pkl)

🧠 Tech Used
Python Libraries

numpy

pandas

matplotlib

scikit-learn

joblib

tkinter

Pillow (PIL)

ML Algorithm

Linear Regression

📊 Dataset Used

Filename: student_info.csv

Columns:

study_hours

student_marks

Source institution: Unknown / Anonymized (Kaggle Open Dataset)
(Public dataset, no official institute information provided)

🚀 How to Run the Project
1. Clone the repository
git clone (https://github.com/MudasirIqbal-Rana/Cradit_Card_Fraud_detection.git)
cd student-marks-predictor

2. Install required libraries
pip install numpy pandas matplotlib scikit-learn joblib pillow

3. Train the Model (Optional)

Run this file if you want to retrain the model:

train_model.py

4. Run the GUI Application
python gui_app.py

🖼 GUI Preview

Takes student name

Takes study hours

Predicts expected marks

Shows an image at the top

Displays output in real-time

📁 Files in This Project
File	Description
student_info.csv	Training dataset
train_model.py	ML model training code
student_marks_predictor.pkl	Saved trained model
gui_app.py	Tkinter GUI application
students2.jpeg	Image used in GUI
README.md	Project documentation
📌 Model Accuracy

The model accuracy (R² score) can be printed using:

lr.score(X_test, y_test)

✨ Features

Predicts marks with good accuracy

Easy-to-use graphical interface

Includes data cleaning & visualization

Uses machine learning model trained on real data

📬 Author

Mudasir Iqbal
Machine Learning Beginner | Python Developer
