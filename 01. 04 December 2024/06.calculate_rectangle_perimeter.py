# Author: Minhazul Kabir
# Email: mdminhazulkabir@gmail.com
"""
1. Calculate the Area of a Circle
Question: Write a Python program to calculate the area of a circle given its radius.
    Input: Radius of the circle
    Process: Area = π × radius² (Use π ≈ 3.1416)
    Output: The area of the circle
"""
# Input: Length and Width of the rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Process: Perimeter = 2 × (Length + Width)
perimeter = 2 * (length + width)

# Output: The perimeter of the rectangle
print(f"The perimeter of the rectangle is: {perimeter}")

# Output: The result type of perimeter of the rectangle
print(f"The result type of the perimeter is: {type(perimeter)}")