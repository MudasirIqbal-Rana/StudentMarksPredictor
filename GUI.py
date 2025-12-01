import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np
from PIL import Image, ImageTk

# Load your trained model
model = joblib.load("student_marks_predictor.pkl")

# Predict Function
def predict_marks():
    try:
        name = entry_name.get()
        hours = float(entry_hours.get())

        if name.strip() == "":
            messagebox.showwarning("Missing Name", "Please enter the student's name.")
            return
        prediction = model.predict([[hours]])[0]
        result_label.config(text=f"{name}'s Predicted Marks is : {prediction:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")


# ------------------ GUI SETUP ------------------ #

root = tk.Tk()
root.title("Student Marks Predictor")
root.geometry("400x300")
root.config(bg="green")

root.minsize(800,600)

try:
    top_img = Image.open("students2.jpeg")
    top_img = top_img.resize((300, 150))
    top_img = ImageTk.PhotoImage(top_img)
    top_label = tk.Label(root, image=top_img, bg="white")
    top_label.pack(pady=10)
except:
    pass 

title = tk.Label(root, text="Student Marks Predictor", font=("Times New Roman", 18, "bold"), bg="blue")
title.pack(pady=25)

frame = tk.Frame(root, bg="white")
frame.pack()

label_name = tk.Label(frame, text="Enter your name:",font=("Times New Roman",14), bg="white")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(frame, font=("Times New Roman",14), width=10)
entry_name.grid(row=0, column=1)

label_hours = tk.Label(frame, text="Enter Study Hours:", font=("Arial", 14), bg="white")
label_hours.grid(row=1, column=0, padx=10, pady=10)

entry_hours = tk.Entry(frame, font=("Arial", 14), width=10)
entry_hours.grid(row=1, column=1)

predict_button = tk.Button(root, text="Predict Marks", font=("Arial", 14), command=predict_marks, bg="#0078FF", fg="white")
predict_button.pack(pady=20)

result_label = tk.Label(root, text="Predicted Marks: ", font=("Arial", 16), bg="#E9F8FF")
result_label.pack()

root.mainloop()
