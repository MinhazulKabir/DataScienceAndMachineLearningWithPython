def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numeric values.")
    else:
        print(f"The result of dividing {num1} by {num2} is: {result}")


# Call the function
divide_numbers()
