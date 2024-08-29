def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI).

    :param weight: Weight in kilograms.
    :param height: Height in meters.
    :return: BMI as a float.
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """
    Determine the BMI category.

    :param bmi: The BMI value.
    :return: The category as a string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError as e:
        print(f"Error: {e}")