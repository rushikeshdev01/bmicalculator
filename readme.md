
## BMI Calculator Application

This application calculates the Body Mass Index (BMI) based on user-provided weight and height values and categorizes the result. It uses `tkinter` for the graphical user interface.     

### Requirements

- Python 3.x
- `tkinter` (standard library)

### Functions

#### `calculate_bmi(weight, height)`

**Purpose**: Computes the Body Mass Index (BMI) based on weight and height.

**Parameters**:
- `weight` (float): Weight in kilograms.
- `height` (float): Height in centimeters.

**Returns**: 
- `float`: The BMI value.

**Raises**:
- `ValueError`: If the height is less than or equal to zero.

**Example**:
```python
bmi = calculate_bmi(70, 175)  # Weight in kg, Height in cm
```

#### `get_bmi_category(bmi)`

**Purpose**: Determines the BMI category based on the calculated BMI value.

**Parameters**:
- `bmi` (float): The calculated BMI value.

**Returns**:
- `str`: The BMI category ("Underweight", "Normal weight", "Overweight", "Obesity").

**Example**:
```python
category = get_bmi_category(22.5)  # BMI value
```

#### `on_calculate()`

**Purpose**: Handles the calculation of BMI and updates the result display.

**Functionality**:
- Retrieves user input from the weight and height fields.
- Calculates the BMI and its category.
- Updates the result label with the BMI and category.
- Displays an error message if the input values are invalid.

**Example**:
```python
on_calculate()  # Triggered by the button click
```

### GUI Components

- **Main Window**:
  - Created using `tk.Tk()`.
  - Title set to "BMI Calculator".

- **Weight Input**:
  - Label: "Enter your weight (kg):".
  - Entry Field: User inputs weight in kilograms.

- **Height Input**:
  - Label: "Enter your height (cm):".
  - Entry Field: User inputs height in centimeters.

- **Calculate Button**:
  - Text: "Calculate BMI".
  - On Click: Calls `on_calculate()`.

- **Result Display**:
  - Label: Displays the calculated BMI and category.
  - Font: Helvetica, size 14.

### Example Usage

1. **Run the Application**: Execute the Python script to open the BMI calculator window.

2. **Input Values**:
   - Enter weight in kilograms.
   - Enter height in centimeters.

3. **Calculate**:
   - Click the "Calculate BMI" button to see the BMI and category displayed.

4. **Error Handling**:
   - If invalid inputs are provided, an error message will be displayed.

### Code Example

```python
import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    if height <= 0:kHere’s the documentation for the BMI calculator application using `tkinter`. This includes descriptions of the functions, classes, and overall usage of the code.

---

## BMI Calculator Application

This application calculates the Body Mass Index (BMI) based on user-provided weight and height values and categorizes the result. It uses `tkinter` for the graphical user interface.

### Requirements

- Python 3.x
- `tkinter` (standard library)

### Functions

#### `calculate_bmi(weight, height)`

**Purpose**: Computes the Body Mass Index (BMI) based on weight and height.

**Parameters**:
- `weight` (float): Weight in kilograms.
- `height` (float): Height in centimeters.

**Returns**: 
- `float`: The BMI value.

**Raises**:
- `ValueError`: If the height is less than or equal to zero.

**Example**:
```python
bmi = calculate_bmi(70, 175)  # Weight in kg, Height in cm
```

#### `get_bmi_category(bmi)`

**Purpose**: Determines the BMI category based on the calculated BMI value.

**Parameters**:
- `bmi` (float): The calculated BMI value.

**Returns**:
- `str`: The BMI category ("Underweight", "Normal weight", "Overweight", "Obesity").

**Example**:
```python
category = get_bmi_category(22.5)  # BMI value
```

#### `on_calculate()`

**Purpose**: Handles the calculation of BMI and updates the result display.

**Functionality**:
- Retrieves user input from the weight and height fields.
- Calculates the BMI and its category.
- Updates the result label with the BMI and category.
- Displays an error message if the input values are invalid.

**Example**:
```python
on_calculate()  # Triggered by the button click
```

### GUI Components

- **Main Window**:
  - Created using `tk.Tk()`.
  - Title set to "BMI Calculator".

- **Weight Input**:
  - Label: "Enter your weight (kg):".
  - Entry Field: User inputs weight in kilograms.

- **Height Input**:
  - Label: "Enter your height (cm):".
  - Entry Field: User inputs height in centimeters.

- **Calculate Button**:
  - Text: "Calculate BMI".
  - On Click: Calls `on_calculate()`.

- **Result Display**:
  - Label: Displays the calculated BMI and category.
  - Font: Helvetica, size 14.

### Example Usage

1. **Run the Application**: Execute the Python script to open the BMI calculator window.

2. **Input Values**:
   - Enter weight in kilograms.
   - Enter height in centimeters.

3. **Calculate**:
   - Click the "Calculate BMI" button to see the BMI and category displayed.

4. **Error Handling**:
   - If invalid inputs are provided, an error message will be displayed.

### Code Example

```python
import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return weight / ((height / 100) ** 2)

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

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Enter your weight (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your height (cm):").grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Helvetica", 14)).grid(row=3, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Calculate BMI", command=on_calculate).grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
```

---

This documentation provides a detailed overview of the BMI calculator application, including function descriptions, GUI components, and an example usage scenario. Let me know if you need any further details or modifications!
        raise ValueError("Height must be greater than zero")
    return weight / ((height / 100) ** 2)

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

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Enter your weight (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your height (cm):").grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Helvetica", 14)).grid(row=3, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Calculate BMI", command=on_calculate).grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
```
