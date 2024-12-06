# Author: Minhazul Kabir
# Email: mdminhazulkabir@gmail.com
"""
1. Calculate the Area of a Circle
Question: Write a Python program to calculate the area of a circle given its radius.
    Input: Radius of the circle
    Process: Area = π × radius² (Use π ≈ 3.1416)
    Output: The area of the circle
"""

# Input: Radius of the circle
radius = int(input("Enter the radius of the circle: "))

# Process: Area = π × radius²
area = 3.1416 * radius * radius

# Output: The area of the circle
print(f"The area of the circle with radius {radius} is: {area}")

# Output: Type class of radius and area checking
print(f"Type of radius {type(radius)} and type of area {type(area)}")
