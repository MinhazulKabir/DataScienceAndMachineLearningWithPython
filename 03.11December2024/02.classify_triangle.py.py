"""
Name: Md. Minhazul Kabir
Email: mdminhazulkabir@gmail.com
Problem Name: 02. Classify Triangle by Sides
"""

side1 = float(input("Enter the first side length: "))
side2 = float(input("Enter the second side length: "))
side3 = float(input("Enter the third side length: "))


if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The given sides do not form a valid triangle.")
