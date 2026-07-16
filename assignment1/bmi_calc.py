def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values")

    bmi = weight / (height ** 2)
    return round(bmi, 2)

try:
    w = float(input("Enter weight in kg: "))
    h = float(input("Enter height in meters: "))
    result = calculate_bmi(w, h)
    print("BMI:", result)
except ValueError as e:
    print("Error:", e)