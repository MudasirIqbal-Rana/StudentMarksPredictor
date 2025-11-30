# Cradit_Card_Fraud_detection
📘 Student Marks Prediction Using Linear Regression

This project builds a Machine Learning model that predicts a student's marks based on the number of study hours using Linear Regression.
The dataset contains two columns:

study_hours

student_marks

The model is trained using scikit-learn, visualized with Matplotlib, and cleaned/processed with Pandas.

📂 Dataset

The dataset consists of study hours and marks obtained by different students.
Some values in the study_hours column are missing, which are handled using mean imputation.

Example:

study_hours,student_marks
6.83,78.5
6.56,76.74
,78.68
5.67,71.82
...

🧹 Data Preprocessing

Steps performed:

Load the dataset using pandas.read_csv()

Check missing values

Fill missing study hours using column mean:

df2 = df.fillna(df.mean())


Split dataset into features (X) and labels (y)

Train-Test split:

train_test_split(X, y, test_size=0.2, random_state=51)

📊 Data Visualization

A scatter plot is used to show the relationship between study hours and marks:

plt.scatter(df.study_hours, df.student_marks)
plt.xlabel("Student study hours")
plt.ylabel("Student marks")
plt.title("Scatter Plot")

🤖 Model Used — Linear Regression

The model is built using:

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)


Model parameters:

Coefficient (m) → slope

Intercept (c) → y-intercept

Prediction example:

lr.predict([[4]])  # Predict marks for 4 hours of study


Model accuracy:

lr.score(X_test, y_test)

📈 Results

A final comparison of actual vs predicted values is created:

pd.DataFrame(np.c_[X_test, y_test, y_predict], 
             columns=["study_hours", "student_marks", "y_predict"])


A line plot of the trained model is added for visualization.

💾 Saving and Loading the Trained Model

The model is saved using joblib:

import joblib
joblib.dump(lr, "student_marks_predictor.pkl")


To load and test:

model = joblib.load("student_marks_predictor.pkl")
model.predict([[5]])

🛠️ Requirements

Install required libraries:

pip install numpy pandas matplotlib scikit-learn joblib


Or using Google Colab (recommended):

!pip install scikit-learn joblib

▶️ How to Run the Code

Upload the dataset in Google Colab using:

from google.colab import files
files.upload()


Run the notebook cells in order.

Train the model.

Predict marks for new study hours.
