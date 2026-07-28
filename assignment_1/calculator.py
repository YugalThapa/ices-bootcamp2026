def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def main():
    print("Welcome to the calculator!")
    print("This calculator can add, subtract, multiply, and divide two numbers.")
    print("-"*30)

    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")

            if operation == '+':
                print(f"The result is: {add(a, b)}")
            elif operation == '-':
                print(f"The result is: {subtract(a, b)}")
            elif operation == '*':
                print(f"The result is: {multiply(a, b)}")
            elif operation == '/':
                if b == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The result is: {divide(a, b)}")
            else:
                print("Invalid operation. Please try again.")

            cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()