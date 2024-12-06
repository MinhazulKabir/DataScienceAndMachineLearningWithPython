# Author: Minhazul Kabir
# Email: mdminhazulkabir@gmail.com
"""
1. Calculate the Area of a Circle
Question: Write a Python program to calculate the area of a circle given its radius.
    Input: Radius of the circle
    Process: Area = π × radius² (Use π ≈ 3.1416)
    Output: The area of the circle
"""
# Input: Three numbers entered by the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Process: Average = (number1 + number2 + number3) / 3
average = (num1 + num2 + num3) / 3

# Output: The average of the three numbers
print(f"The average of the numbers {num1}, {num2}, {num3} is: {average}")

# Output: The type of all input variables and the result variable
print(f"The type of num1: {type(num1)}, num2: {type(num2)}, num3: {type(num3)}, and the average: {type(average)}")