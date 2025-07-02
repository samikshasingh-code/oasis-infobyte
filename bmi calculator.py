import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# ------------------ BMI Logic ------------------ #
def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# ------------------ Save Data ------------------ #
def save_data(weight, height, bmi, category):
    file_exists = os.path.isfile('bmi_data.csv')
    with open('bmi_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Weight(kg)', 'Height(m)', 'BMI', 'Category'])
        writer.writerow([weight, height, bmi, category])

# ------------------ GUI Functions ------------------ #
def on_calculate():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers.")
            return
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        label_result.config(text=f"BMI: {bmi}\nCategory: {category}")
        save_data(weight, height, bmi, category)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def view_history():
    if not os.path.isfile('bmi_data.csv'):
        messagebox.showinfo("No Data", "No historical data available.")
        return

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")

    tree = ttk.Treeview(history_window, columns=('Weight', 'Height', 'BMI', 'Category'), show='headings')
    tree.heading('Weight', text='Weight (kg)')
    tree.heading('Height', text='Height (m)')
    tree.heading('BMI', text='BMI')
    tree.heading('Category', text='Category')

    with open('bmi_data.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            tree.insert('', tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)

# ------------------ GUI Layout ------------------ #
root = tk.Tk()
root.title("BMI Calculator")

label_heading = tk.Label(root, text="BMI Calculator", font=("Arial", 16))
label_heading.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

label_weight = tk.Label(frame_input, text="Weight (kg):")
label_weight.grid(row=0, column=0, padx=5, pady=5)
entry_weight = tk.Entry(frame_input)
entry_weight.grid(row=0, column=1, padx=5, pady=5)

label_height = tk.Label(frame_input, text="Height (m):")
label_height.grid(row=1, column=0, padx=5, pady=5)
entry_height = tk.Entry(frame_input)
entry_height.grid(row=1, column=1, padx=5, pady=5)

button_calculate = tk.Button(root, text="Calculate BMI", command=on_calculate)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

button_history = tk.Button(root, text="View History", command=view_history)
button_history.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=root.quit)
button_exit.pack(pady=5)

root.mainloop()
