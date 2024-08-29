import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return weight / ((height/100) ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def on_calculate():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        result_text.set(f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
tk.Label(root, text="Enter your weight (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your height (cm):").grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Helvetica", 14)).grid(row=3, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Calculate BMI", command=on_calculate).grid(row=2, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
