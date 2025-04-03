def basic_calculator():
    try:
        # Ask the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Ask the user for the operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please use +, -, *, or /.")
            return

        # Print the result
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Run the calculator
basic_calculator()
